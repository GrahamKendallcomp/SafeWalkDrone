import sys
import os
import track
from pathlib import Path
import multiprocessing as m


from ground_station.groundStation import groundStation
from ground_station.makeInstruction import makeInstruction
from ground_station.commands import *







def main():
    #sitl, drone = groundStation.init()
    bboxlist = []
    missionDone = False
    yolo = track.trackclass(bboxlist)
    altitude = 2
    yoloprocess = m.Process(target = yolo.run)
    yoloprocess.start()

    #commands.arm_and_takeoff(drone, altitude)

    while(True):
        bboxlist = yolo.returnBboxList() #contains all the tracking data
        m.yolo.returnBBoxList()
        print(bboxlist)
        #use commands.py  drone commands for drone control
        #pass
        if (missionDone):
            break

    #groundStation.shutdown(sitl, drone)
    #Yolov5Thread.exit()
    

if __name__ == "__main__":
     main()


