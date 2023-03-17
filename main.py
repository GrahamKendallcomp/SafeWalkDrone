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
        #use commands.py  drone commands for drone control
        #pass
        if (missionDone):
            break
    #groundStation.shutdown(sitl, drone)
    #Yolov5Thread.exit()


def makeGUI():
    root = tk.Tk()
    my_gui = GUI(root)
    root.mainloop()






class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Drone Instructions")
        master.config(bg='light sky blue')

        master.geometry('1200x200')
        self.label = tk.Label(master, text="No Instructions Yet.", font=('courier',15), highlightbackground="light sky blue", highlightcolor='light sky blue', bg= 'light sky blue')
        self.label.place(relx=0.5, rely=0.5, anchor='center')
        self.label.pack()
        self.data = bboxlist
        self.update_label()

    def update_label(self):
        # Do some calculations to get the new value
        new_value = parseBboxList()
        #print(new_value)
        # Update the label with the new value
        self.label.config(text=new_value)
        # Schedule the update function to be called again in 1000 milliseconds (1 second)
        self.master.after(500, self.update_label)


def parseBboxList()->str:
    #bboxlist = bboxlist
    data = bboxlist
    #print(bboxlist)
    wordlist = []
    for bboxes in bboxlist:
        bboxes = tuple(bboxes)
        print(bboxes[3] - bboxes[1])
        output = instruct.dataForDisplay(bboxes)
        word = "ID: " + str(bboxes[4]) + "," + str(output[0]) +' ft away' + " move laterally " +  str(output[1]) +'ft ' + "move vertically " + str(output[2]) + ' ft' + '\n'
        wordlist.append(word)             
    print(wordlist)
    if (wordlist != []):
        returnString = ''.join(wordlist)
        return returnString
    else:
        return "No Data Yet"







if __name__ == "__main__":
    main()
    