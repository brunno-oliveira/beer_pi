
import gspread
from datetime import datetime
from w1thermsensor import W1ThermSensor
from oauth2client.service_account import ServiceAccountCredentials


class GSheet:
    def __init__(self):
        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive",
        ]
        self.cred = "/home/pi/git/beer_pi/creds.json"
        self.client = None
        self.connect()

    def connect(self):
        print('Connection do GSheets..')
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            self.cred, self.scope)
        self.client = gspread.authorize(creds)

    def update(
            self,
            sheet_key: str = "1x0qI0HRQstLbYiUE4fnWGu1oguK0bK9Pp3lR7UwqlWQ"):
        sheet = self.client.open_by_key(
            sheet_key).sheet1

        sensors = ['3c01d607ca23', '3c01b5568463']

        columns = {
            'A': 'TIMESTAMP',
            'B': 'DATE',
            'C': 'TIME',
            'D': 'SENSOR',
            'E': 'TEMPERATURA',
            'F': 'INFO'}

        sensores = ['INTERNO', 'EXTERNO']

        now = datetime.now()
        print('Updating rows..')
        for sensor in W1ThermSensor.get_available_sensors():
            # Fita vermelha
            if sensor.id == '3c01b5568463':
                sensor_name = sensores[0]
            else:
                sensor_name = sensores[1]
            info = ''
            values = [
                datetime.timestamp(now),
                str(now.date()),
                str(now.time()),
                sensor_name,
                sensor.get_temperature(),
                info
            ]
            print('VALUES:')
            print(values)
            sheet.append_row(values)

        print('done')


if __name__ == "__main__":
    GSheet().update()
