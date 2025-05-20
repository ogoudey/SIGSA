import w_agents
from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, function_tool, trace
from pydantic import validate_arguments, ConfigDict
import sheets
import asyncio
from typing import Any
from gspread.worksheet import Worksheet

worksheet = sheets.main()

### Execution-level functions ###


@dataclass
class Context:
    info: str="default"

### Tool-level functions ###
@function_tool
async def manufacture_tool(instructions: str):
    return await w_agents.manufacture(instructions)


    

  
@function_tool
async def execute(python_str: str):
    exec(python_str, {"worksheet": worksheet})
    return "Python executed successfully."



async def main(): 
    context=Context() 
    executor_agent = Agent[Context](name="executor", instructions="You will be given some python code. Call `execute` on the python, and make sure the arguments align. That is, `worksheet` is already defined in local scope -- it should be a permissive gspread worksheet.", tools=[execute])

      
    agent = Agent[Context](
        name="worksheet_worker",
        instructions="""Your job is to manufacture a tool that takes the Google Sheets Worksheet with full permissions/credentials and follows the user's request. When you request a tool to be manufactured, give detailed instructions. Clarify in your instructions that the tool must use `worksheet` as a given name for a permissive gspread worksheet -- no need to get credentials. It should be as simple as possible.\nYou also have an `execute` tool to execute python code. Execute the user's request by calling `execute` on generated python code. If you execute a function definition, also execute the function call. Keep in mind, the worksheet is accessed with `worksheet`, and (one last thing), the user can see what you `print()` in execution, not the actual code - don't draw attention to this functionality, treat print() like your response.""",
        tools=[manufacture_tool, execute]
    )        
            
     
        #executor_agent.as_tool(tool_name="execute_manufactured_tool", tool_description="Send the manufactured tool (e.g. python code and markdown) to an Agent that will execute it intelligently.")])
    convo=""
    while True:
        result = await Runner.run(agent, str(convo) + input("--> "), context=context)
        print(result.final_output)
        convo = result.to_input_list()
            

if __name__ == "__main__":
    asyncio.run(main())
