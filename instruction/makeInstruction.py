import sendInstruction
import math as m

#bbox_left =output[0]
#bbox_top  = output[1]
#bbox_w = output[2] - output[0]
#bbox_h = output[3] - output[1]
#output[4] = id

#Some non-Class functions
piCameraResolution = (640,480)

def getBboxCentre(bbox):
        return (((bbox[2]-bbox[0])/2 + bbox[0]), (((bbox[3]-bbox[1])/2)+bbox[1]))

def checkHeight(bbox):
        height = bbox[3] - bbox[1]
        if((height > 250 ) & (height < 180)):
            return (True,height)
        else:
            return (False,height)


def isCentre(bbox,centreScreen):
    x,y = True, True
    bboxCentre = getBboxCentre(bbox)
    ## is the BBox Centred? or Close enough to the centre for noise?
    if((bboxCentre[0],bboxCentre[1] != centreScreen[0],centreScreen[1])):
        return x,y
    if(m.abs(bboxCentre[0] - centreScreen[0]) < 10) & ((m.abs(bboxCentre[1] - centreScreen[1])) ):
        return x,y
    #if its too far from the centre
    else:
        if (m.abs(bboxCentre[0] - centreScreen[0]) > 10):
            x = False
        if (m.abs(bboxCentre[1] - centreScreen[1]) > 10):
            y = True
        return x,y



class makeInstruction:
    

    def __init__(self,
                 frame,
                 bbox,
                 id,
                 lastFrame


    ):
        self.frame = 0
        self.lastFrame = []

    def update(self,bbox):
        self.bbox = bbox
        self.frame += 1
        self.id = bbox[4]
        self.lastFrame.append((((bbox[2]-bbox[0])/2 + bbox[0]), (((bbox[3]-bbox[1])/2)+bbox[1])))

    #Deadzone is defined as the area covered by 40% of the length from the midpoint to the edges of the screen
    #in both Horizontal and vertical axises
    #Xlimits =(128-512)
    #Ylimits = (96-384)
    #True is bad.
    #def checkDeadZone():
    #   result = (True,True)
    #    tempX = getBboxCenter(bbox)[0]
    #    tempY = getBboxCenter(bbox)[1]
    #    if((tempX > 128) & (tempX<512)):
    #        result[0] = False
    #    if((tempY> 96) & (tempY <384)):
    #        result[1] = False
    #    return result

    #Some known known parameter will be the set distance to keep
    #temp pixel height = 200 pixels.
    
        
    def vectorToSubject(self):
        self.checkHeight


    def run(self):
        instruction = []
        centreScreen = (piCameraResolution[0]/2,piCameraResolution[1]/2)
        
        #Algorithm
        #Check Height
        #Check Distance from Centre
        #Trajectory
        if(checkHeight(self, self.bbox)[0]):
            

        


        
        




        



        
            

        



    
    









