import threading as t
import sys
import os
import track
from pathlib import Path


from ground_station.groundStation import groundStation
from ground_station.makeInstruction import makeInstruction
from ground_station.commands import *

bboxlist = []
yolo = track.trackclass(bboxlist)




def main():
    if __name__ == "__main__":
        #sitl, drone = groundStation.init()
        missionDone = False
        altitude = 2
        yolothread = t.Thread(target = yolo.main)
        yolothread.daemon = True
        yolothread.start()

        #commands.arm_and_takeoff(drone, altitude)

        while(True):
            bboxs = yolo.bboxlist #contains all the tracking data 
            #use commands.py  drone commands for drone control
            #pass
            if (missionDone):
                break

        groundStation.shutdown(sitl, drone)
        #Yolov5Thread.exit()
        
main()