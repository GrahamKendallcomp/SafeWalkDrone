import groundStation
import commands 
import time

def main():
    if __name__ == "__main__":
        sitl, drone = groundStation.init()
        altitude = 1
        commands.arm_and_takeoff(drone, altitude)
        time.sleep(10)
        commands.arm_and_takeoff(drone, 0)

        groundStation.shutdown(sitl, drone)