import sys
import os
import track
from pathlib import Path
import multiprocessing as m
import socket
import pickle

from ground_station.groundStation import groundStation
from ground_station.makeInstruction import makeInstruction
from ground_station.commands import *






def main():
    bboxlist = []
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 8888))
    yolo = track.trackclass(bboxlist)
    yoloprocess = m.Process(target = yolo.run)
    
    #sitl, drone = groundStation.init()
    missionDone = False
    altitude = 2
    yoloprocess.start()
    #commands.arm_and_takeoff(drone, altitude)

    while(True):
        data = sock.recvfrom(1024)
        bboxlist = pickle.loads(data[0])
        
        #use commands.py  drone commands for drone control
        #pass
        if (missionDone):
            break
    sock.close()
    #groundStation.shutdown(sitl, drone)
    #Yolov5Thread.exit()
    

if __name__ == "__main__":
    main()
    


