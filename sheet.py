
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

class GSheet:
    def __init__(self):
        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive",
        ]
        self.cred = "creds.json"
        self.client = None
        self.connect()

    def connect(self):
        print('Connection do GSheets..')
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.cred, self.scope)
        self.client = gspread.authorize(creds)

    def update(
        self, 
        temp: float, 
        sheet_key: str = "1x0qI0HRQstLbYiUE4fnWGu1oguK0bK9Pp3lR7UwqlWQ"):
        sheet =  self.client.open_by_key(sheet_key).sheet1  # Open the spreadhseet

        columns = {
            'A': 'TIMESTAMP',
            'B': 'DATE',
            'C': 'TIME',
            'D': 'SENSOR',
            'E': 'TEMPERATURA',
            'F': 'INFO'}

        sensores = ['INTERNO', 'EXTERNO','TESTE']

        now = datetime.now()

        print('Updating row..')

        values =  [
                    datetime.timestamp(now),
                    str(now.date()), 
                    str(now.time()), 
                    'TESTE',
                    temp,
                    'sensor na mesa'
                ]
        print('VALUES:')
        print(values)
        sheet.append_row(values)

        print('done')

if __name__ == "__main__":
    GSheet().update(temp=25.5)
    
