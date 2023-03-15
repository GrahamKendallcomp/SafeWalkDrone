import math as m

#bbox_left =output[0]
#bbox_top  = output[1]
#bbox_w = output[2] - output[0]
#bbox_h = output[3] - output[1]
#output[4] = id

#Some non-Class functions
piCameraResolution = (640,480)
cameraAngle = 30
psi = 1
centreScreen = (piCameraResolution[0]/2,piCameraResolution[1]/2)

class makeInstruction:

    def getBboxCentre(bbox):
            return (((bbox[2]-bbox[0])/2 + bbox[0]), (((bbox[3]-bbox[1])/2)+bbox[1]))

    def checkPixelHeight(bbox):
            height = bbox[3] - bbox[1]
            if((height > 250 ) & (height < 180)):
                return (True,height)
            else:
                return (False,height)
            
    #Parallax Correction for Height
    def pHeightRealHeight(pixels):
        theta = cameraAngle
        realPHeight =  pixels * 1/(m.cos(theta) / (1 - m.sin(theta)))
        return realPHeight


    #Very rough estimate, Based on a 1.8m tall person
    def pixelHeightDistanceAway(pixels):
        return 3*pixels + 6




    #Returns Distance to the Drone from the subject
    def distanceToDrone(self,height):
        return self.pHeightRealHeight(height) * m.tan(psi)


    #Vector from the drone to the subject in meters
    #mavLink uses x forward, y to the right, z ascend.
    #Should be in 'meters' approximation
    def vectorInstruction(self,bbox):
        y,z =  ((self.getBboxCentre(bbox) - centreScreen))
        x = self.distanceToDrone(self.pHeightRealHeight(self.checkPixelHeight(bbox)[1]))
        return (x,y,z)


        

    def isCentre(self,bbox,centreScreen):
        x,y,x2,y2 = True, True,0,0
        bboxCentre = self.getBboxCentre(bbox)
        ## is the BBox Centred? or Close enough to the centre for noise?
        if((bboxCentre[0],bboxCentre[1] == centreScreen[0],centreScreen[1])):
            return x,y,x2,y2
        if(m.abs(bboxCentre[0] - centreScreen[0]) < 10) & ((m.abs(bboxCentre[1] - centreScreen[1])) ):
            return x,y,x2,y2
        #if its too far from the centre
        else:
            if (m.abs(bboxCentre[0] - centreScreen[0]) > 10):
                x = False
            if (m.abs(bboxCentre[1] - centreScreen[1]) > 10):
                y = True
            return x,y




    

    def __init__(self,
                 frame,
                 bbox,
                 id,
                 lastFrame,
                 newInstruction


    ):
        self.frame = 0
        self.lastFrame = []

    def update(self,bbox):
        self.bbox = bbox
        self.frame += 1
        self.id = bbox[4]
        self.lastFrame.append((((bbox[2]-bbox[0])/2 + bbox[0]), (((bbox[3]-bbox[1])/2)+bbox[1])))
        self.newInstruction = self.vectorInstruction(self.bbox)





                 


             
            

        


        
        




        



        
            

        



    
    









