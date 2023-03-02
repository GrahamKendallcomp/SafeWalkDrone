import groundStation
#import commands 
import threading as t
from .. import track



def main():
    if __name__ == "__main__":
        sitl, drone = groundStation.init()
        missionDone = False
        altitude = 2
        Yolov5Thread = t.Thread(target = track.main , args =track.parse_opt)
        Yolov5Thread.start()
        track.main(track.opt)




        #commands.arm_and_takeoff(drone, altitude)

        while(True):
            #put constant yolov5 detection here
            #use commands.py  drone commands for drone control
            pass
            if (missionDone):
                break

        groundStation.shutdown(sitl, drone)
        Yolov5Thread.exit()
        
main()