import time
import busio
import adafruit_adxl34x
import board
import csv
import adafruit_si7021
i2c = busio.I2C(board.SCL, board.SDA)

accelometer = adafruit_adxl34x.ADXL345(i2c)
sensor = adafruit_si7021.SI7021(i2c)
i=0
hutname = ''
readfile = 'accelandmicroclimate' + hutname + '.csv'
  
while i<720:
    with open(readfile, 'a', newline='') as csvfile:
        fieldnames = ['x', 'y', 'z', 'celsius', 'relativehumid']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'x': accelometer.acceleration[0], 'y': accelometer.acceleration[1], 'z': accelometer.acceleration[2], 'celsius': sensor.temperature, 'relativehumid': sensor.relative_humidity})
    time.sleep(5)
    i = i+1
