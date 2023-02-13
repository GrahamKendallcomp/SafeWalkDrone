import dronekit_sitl
from dronekit import connect, VehicleMode
from paramiko import SSHClient

def init():
    print("Creating ssh connection to RPi")
    client = SSHClient()
    client.connect('10.242.215.212', username='stephen', password='4thyearproject2022!')
    
    print("Setting up MAVProxy")
    stdin, stdout, stderr = client.exec_command('mavproxy.py --out=tcpin:0.0.0.0:14550')
    print(stdin)
    print(stdout)
    print(stderr)

    print( "Start simulator (SITL)") 
    sitl = dronekit_sitl.start_default()

    connection_string = "tcp:10.242.215.212:14550"
    print(("Connecting to vehicle on: %s" % (connection_string,))) 
    vehicle = connect(connection_string, wait_ready=True)
    print( "Get some vehicle attribute values:") 
    print( " GPS: %s" % vehicle.gps_0) 
    print( " Battery: %s" % vehicle.battery) 
    print( " Last Heartbeat: %s" % vehicle.last_heartbeat) 
    print( " Is Armable?: %s" % vehicle.is_armable) 
    print( " System status: %s" % vehicle.system_status.state) 
    print( " Mode: %s" % vehicle.mode.name ) 

    return sitl, vehicle, client

def shutdown(sitl, vehicle, rpiClient):
    print('Closing vehicle connection')
    vehicle.close()
    rpiClient.exec_command('exit')

    print("Closing ssh connection")
    rpiClient.close()

    print("Shutting down simulator")
    sitl.stop()