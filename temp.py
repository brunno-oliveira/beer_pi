# %%
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# %%
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# %%
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


# %%
sheet = client.open_by_key("1x0qI0HRQstLbYiUE4fnWGu1oguK0bK9Pp3lR7UwqlWQ").sheet1  # Open the spreadhseet

# %%
data = sheet.get_all_records()  # Get a list of all records
print(data)

# %%
d = [dict(v) for v in data]

# %%
columns = {
    'A': 'TIMESTAMP',
    'B': 'SENSOR',
    'C': 'TEMPERATURA',
    'D': 'INFO'}

sensores = ['INTERNO', 'EXTERNO']

# UPDATE
sheet.append_row([8,'INTERNO',28,''])
