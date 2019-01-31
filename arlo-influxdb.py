#!/usr/bin/python

from pyarlo import PyArlo
from influxdb import InfluxDBClient

# INFLUXDB CONNECTION INFO
host = "192.168.1.67"
port = 8086
user = "user"
password = "password" 
dbname = "readings"

# CREATE CLIENT OBJECT
client = InfluxDBClient(host, port, user, password, dbname)

# ARLO CONNECTION INFO
arlo  = PyArlo('user@fake.com', 'password')

# SET VARIABLES
cam = arlo.cameras
cam = len(cam)

# COLLECT & UPLOAD DATA
if cam <> 0:
	for i in range(cam):
		model_id = arlo.cameras[i].model_id
		serial_number = arlo.cameras[i].serial_number
		brightness = arlo.cameras[i].brightness
		battery_level = arlo.cameras[i].battery_level
		signal_strength = arlo.cameras[i].signal_strength
		measurement = "jupitor-" + model_id + "-" + serial_number
		
		data = [
		{
		  "measurement": measurement,
			  "fields": {
				  "battery_level" : battery_level ,
				  "signal_strength" : signal_strength ,
				  "brightness" : brightness
			  }
		  } 
		]
	
		client.write_points(data)
else:
	sys.exit()
