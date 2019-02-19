from pyarlo import PyArlo
from influxdb import InfluxDBClient
import time
import sys

# INFLUXDB CONNECTION INFO
host = "192.168.1.67"
port = 8086
user = "writer"
password = "password" 
dbname = "database_name"

# CREATE CLIENT OBJECT
client = InfluxDBClient(host, port, user, password, dbname)

# ARLO CONNECTION INFO
arlo  = PyArlo('email@address.com', 'password')

def writeData(i,base):
	
	model_id = arlo.cameras[i].model_id
	serial_number = arlo.cameras[i].serial_number
	battery_level = arlo.cameras[i].battery_level
	signal_strength = arlo.cameras[i].signal_strength
	measurement = base + "-" + model_id + "-" + serial_number
		
	data1 = [
	{
	  "measurement": measurement + "-" + "battery_level",
		  "fields": {
			  "battery_level" : battery_level
		  }
	  } 
	]
	
	data2 = [
	{
	  "measurement": measurement + "-" + "signal_strength",
		  "fields": {
			  "signal_strength" : signal_strength
		  }
	  } 
	]
		
	client.write_points(data1)
	client.write_points(data2)

def main():

	cams = arlo.cameras
	cams = len(cams)

	if cams is not 0:
	
		base = arlo.base_stations[0]
		base = base.properties.get("modelId")
		
		for cam in range(cams):
			writeData(cam,base)
			time.sleep(60)
			
	else:
		sys.exit()
		
if __name__ == "__main__":
	main()
