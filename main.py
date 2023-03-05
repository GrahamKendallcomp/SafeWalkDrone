import threading as t
import sys
import os
import track
from pathlib import Path


from ground_station.groundStation import groundStation
from ground_station.makeInstruction import makeInstruction
from ground_station.commands import *






def main():
    if __name__ == "__main__":
        #sitl, drone = groundStation.init()
        missionDone = False
        altitude = 2
        Yolov5Thread = t.Thread(target = track.run, args = (**vars track.parse_opt()))
        Yolov5Thread.start()

        #commands.arm_and_takeoff(drone, altitude)

        while(True):
            #Yolov5Thread.bbox_list
            #use commands.py  drone commands for drone control
            #pass
            if (missionDone):
                break

        groundStation.shutdown(sitl, drone)
        #Yolov5Thread.exit()
        
main()