import groundStation
import commands 

def main():
    if __name__ == "__main__":
        sitl, drone, rpiClient = groundStation.init()
        missionDone = False
        altitude = 2
        commands.arm_and_takeoff(drone, altitude)
        while(True):
            #put constant yolov5 detection here
            #use commands.py  drone commands for drone control
            pass
            if (missionDone):
                break

        groundStation.shutdown(sitl, drone, rpiClient)