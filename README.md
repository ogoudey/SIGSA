# Semi-Intelligent Google Sheets Agent

## Usage
```
python3 main_agents.py
```
... will start a conversation where the chatbot has access and can perform functions on a Google SpreadSheet.

## Prerequisites
### Install Python Libraries
For authentification with Google and the Agents SDK:
```
pip install openai-agents oauth2client
```
To be used by the agents:
```
pip install gspread # This will be used by the agents
```
### Google Authentification and API Credentials (free)
1. **Set Up Google Sheets API:**
   - Go to the [Google Cloud Console](https://console.developers.google.com/).
   - Create a new project.
   - Enable the Google Sheets API for this project.
   - Create credentials: Choose "Service account" and download the JSON key file. This file is crucial for authenticating API requests.

2. **Share Spreadsheet with Service Account:**
   - Open your Google Spreadsheet.
   - Share it with the service account email (found in your JSON credentials file). This is necessary to allow the service account to access the spreadsheet.
3. **Set Variables:**
   - In `sheets.py`, set the file path of the JSON credentials in `from_json_keyfile_name()`.
   - also in `sheets.py`, set the name of the Google Spreadsheet in `client.open()`.
   
### OpenAI API Key (nearly free)
1. **Set up OpenAI API:**
    - Go to API Keys on the [OpenAI Platform](https://platform.openai.com/api-keys).
    - Create new key and set the key as an environment variable `export OPENAI_API_KEY=<key>`.
    - Fund the key if needed.
