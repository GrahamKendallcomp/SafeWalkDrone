import sys
import os
import track
from pathlib import Path
import multiprocessing as m
import socket
import pickle
import threading as t
import tkinter as tk
import time

from ground_station.groundStation import groundStation
from ground_station.makeInstruction import makeInstruction as instruct
from ground_station.commands import *
import queue





def main():
    global bboxlist 
    bboxlist = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 8888))
    yolo = track.trackclass(bboxlist)
    yoloprocess = m.Process(target = yolo.run)
    tracking_gui = t.Thread(target = makeGUI)
    #sitl, drone = groundStation.init()
    missionDone = False
    altitude = 2
    yoloprocess.start()
    tracking_gui.start()
    
    #commands.arm_and_takeoff(drone, altitude)
    while(True):
        data = sock.recvfrom(1024)
        output = pickle.loads(data[0])
        bboxlist = output
        #print(bboxlist)
        #try:
        ##        q.queue.clear()
            #    for items in bboxlist:
          #         q.put(items)
           #         #print(bboxlist)
        #except:
          #  print()
        #use commands.py  drone commands for drone control
        #pass
        if (missionDone):
            break
    #groundStation.shutdown(sitl, drone)
    #Yolov5Thread.exit()

def makeGUI():
    # create the GUI window
    root = tk.Tk()
    root.title("Drone Instructions")

    # create two instances of the RealTimeDisplay widget
    display1 = RealTimeInstruct(root)
    display1.pack(side='left', padx=200, pady=200)
    #display2 = RealTimeInstruct(root)
    #display2.pack(side='left', padx=200, pady=200)

    # start the GUI event loop
    root.mainloop()




class RealTimeInstruct(tk.Frame):
    def __init__(self, parent):
        #self.queue = q
        #time.sleep(6000)
        super().__init__(parent)
        self.label = tk.Label(self, font=('Courier', 35))
        self.label.pack()
        self.update_Contents()
        
        

    def update_Contents(self):
        string = self.parseBboxList()
        self.label.configure(text=string)
        self.after(500, self.update_Contents)

    def parseBboxList(self)->str:
        #bboxlist = bboxlist
        try: 
            if(bboxlist != []):
                if (bboxlist[0] != []):
                    #print(bboxlist)
                    print(bboxlist[0])
                    temp = instruct.dataForDisplay(bboxlist[0])
                    print(temp)
                    word = "ID: " + str(bboxlist[0][4]) + "move forward " + str(round(temp[0],2)) +'ft' + " move laterally " +  str(round(temp[1],2)) +'ft ' + "move vertically" + str(round(temp[2],2)) + 'ft'
                    #print(word)
                    return word 
                else:
                    return 'potato'
        except:
            pass


    


    

if __name__ == "__main__":
    main()
    