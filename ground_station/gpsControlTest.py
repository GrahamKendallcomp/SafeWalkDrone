import groundStation
import commands 
import time
import dronekit

def main():
    if __name__ == "__main__":
        sitl, drone = groundStation.init()
        altitude = 1
        commands.arm_and_takeoff(drone, altitude)
        a_location = dronekit.LocationGlobalRelative(-34.364114, 149.166022, 30)
        drone.simple_goto(a_location)
        commands.arm_and_takeoff(drone, 0)

        groundStation.shutdown(sitl, drone)