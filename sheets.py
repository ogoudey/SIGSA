"""
1. **Set Up Google Sheets API:**
   - Go to the [Google Cloud Console](https://console.developers.google.com/).
   - Create a new project.
   - Enable the Google Sheets API for this project.
   - Create credentials: Choose "Service account" and download the JSON key file. This file is crucial for authenticating API requests.

2. **Share Spreadsheet with Service Account:**
   - Open your Google Spreadsheet.
   - Share it with the service account email (found in your JSON credentials file). This is necessary to allow the service account to access the spreadsheet.

3. **Install Required Libraries:**
   - Install `gspread` and `oauth2client` using pip:
     ```bash
     pip install gspread oauth2client
     ```

4. **Python Code to Access the Spreadsheet:**
"""
import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials
def clear_worksheet_content(worksheet):
    cell_list = worksheet.range('A1:{}'.format(
        gspread.utils.rowcol_to_a1(worksheet.row_count, worksheet.col_count)
    ))
    for cell in cell_list:
        cell.value = ''
    worksheet.update_cells(cell_list)
    try:
        clear_worksheet_content(worksheet)
    except Exception as e:
        print("Failed to clear worksheet:", e)
# Define the scope
def main():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Load credentials from JSON key file
    credentials = ServiceAccountCredentials.from_json_keyfile_name('recommended-to-do-02a479cff156.json', scope)

    # Authorize the client
    client = gspread.authorize(credentials)

    spreadsheet = client.open('test')

    # Select the first worksheet
    worksheet = spreadsheet.get_worksheet(0)
    return worksheet




    open_by_url(client, 'https://docs.google.com/spreadsheets/d/1ATJ405bTxz8_lwVAHUpmosOa1R_PaFpe5moqkrLdQtQ/edit?gid=0#gid=0')


# Open the spreadsheet by URL
def open_by_url(client, spreadsheet_url):
    spreadsheet = client.open_by_url(spreadsheet_url)

    # Select the first worksheet
    worksheet = spreadsheet.get_worksheet(0)

    # Get all records (as a list of dictionaries)
    records = worksheet.get_all_records()

    print(records)

"""
### Handling Permission Errors or Authentication Issues

- **Authentication Errors:** Ensure that the JSON credentials file is correctly downloaded and its path is specified correctly in the script.
- **Permission Denied:** Double-check that the service account email has been granted access to the Google Sheet. You can verify by going to the "Share" settings of the spreadsheet.

### Checking Spreadsheet Sharing Settings

- Go to the Google Spreadsheet.
- Click on "Share" and ensure that the service account email is listed as having access. Adjust permissions if necessary.
"""
if __name__ == "__main__":
    asyncio.run(main())
