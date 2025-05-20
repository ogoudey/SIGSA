from agents import Agent, Runner, RunContextWrapper, function_tool, trace
from pydantic import BaseModel
import asyncio

class Critique(BaseModel):
    new_instructions: str
    explanation: str


async def manufacture(input_):
    max_attempts = 2
    instructions_0="Assist the user in building what they request."
    manufacturer = Agent(name="manufacturer", instructions=instructions_0)
    critic = Agent(
        name="critic",
        instructions=f"""You are a critic of another LLM chatbot agent (the "manufacturer"). You will receive the user input they received, their instructions, and their output. You will consider their output, and see whether it aligns with the user's intent. If it doesn't, you will modify the agent's instructions accordingly. If no change is needed, set new_instructions to "no change needed" exactly. Don't be too critical! You only have {max_attempts} tries!""",
        output_type=Critique
    )
    
    user_input = input_
    #print("Manufacturer attempts:", end=" ")
    attempts = 0
    while attempts < max_attempts:
        #print("|", end="")
        result = await Runner.run(manufacturer, user_input)
        #print("Manufacturer result:", result.final_output)
        input_ = str(result.to_input_list()) + "\nManufacturer's instructions: " + result.last_agent.instructions + "\nTries left: " + str(max_attempts - attempts)
        critique = await Runner.run(critic, input_)
        if critique.final_output.new_instructions == "no change needed":
            return result.final_output
        else:
            result.last_agent.instructions = critique.final_output.new_instructions
        attempts += 1
    return "Uh oh! Failed."
        
# test contained agents
async def main():
    await manufacture(input("Goal:"))
      
if __name__ == "__main__":
    asyncio.run(main())
    
