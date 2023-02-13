import groundStation
import commands 

def main():
    if __name__ == "__main__":
        sitl, drone = groundStation.init()
        while(True):
            #put constant yolov5 detection here
            #use commands.py  drone commands for drone control
            pass

        groundStation.shutdown(sitl, drone)