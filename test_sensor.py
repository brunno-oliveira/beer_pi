import time
from w1thermsensor import W1ThermSensor

# Test single sensor
sensor = W1ThermSensor()
temperature_in_celsius = sensor.get_temperature()
print('Testing single sensor: {}'.format(temperature_in_celsius))
print()

# Multiple sensors
for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor %s has temperature %.2f" %
          (sensor.id, sensor.get_temperature()))
