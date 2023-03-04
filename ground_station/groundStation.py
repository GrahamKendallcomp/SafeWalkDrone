import dronekit_sitl
from dronekit import connect, VehicleMode
import time
class groundStation():
    def init():
        
        time.sleep(3)
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

        return sitl, vehicle

    def shutdown(sitl, vehicle):
        print('Closing vehicle connection')
        vehicle.close()

        print("Shutting down simulator")
        sitl.stop()