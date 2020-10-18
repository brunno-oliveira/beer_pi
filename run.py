from oauth2client.service_account import ServiceAccountCredentials

from w1thermsensor import W1ThermSensor

from sheet import GSheet

from time import sleep

class Run:
    def get_tempeture(self):
        sensor = W1ThermSensor()
        temperature_in_celsius = sensor.get_temperature()
        return  temperature_in_celsius

    def run(self):
        print('Running...')
        temp = self.get_tempeture()
        print('TEMP: ' + str(temp))
        GSheet().update(temp=temp)

if __name__ == "__main__":
    Run().run()

    