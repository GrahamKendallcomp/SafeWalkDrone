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
centreScreen = (piCameraResolution[0] / 2,piCameraResolution[1] / 2)

class makeInstruction:
     
    def __init__(self):
        pass


    def dataForDisplay(bbox)->tuple:
        
        #print('hello ' + bbox)
        x = pixelHeightDistanceAway(bbox[3] - bbox[1])
        y = pixelLateralDistanceEstimation(vectorInstruction(bbox)[1],(bbox[3]-bbox[1]))
        z = pixelLateralDistanceEstimation(vectorInstruction(bbox)[0],(bbox[3]-bbox[1]))
        if((y or z) == None):
            y=0.00
            z=0.00
        y = round(y,2)
        z = round(z,2)
        return (x,y,z)
            
    def isCentre(bbox,centreScreen):
        x,y,x2,y2 = True, True,0,0
        bboxCentre = getBboxCentre(bbox)
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
    def getBboxCentre(bbox):
        return (((bbox[2]-bbox[0])/2 + bbox[0]), (((bbox[3]-bbox[1])/2)+bbox[1]))  



    #Very rough estimate, Based on a 1.8m tall person/ 6feet
    def pixelHeightDistanceAway(pixels):
        # Define the real-world height of the object in meters or feet
        object_height = 1.82  # meters
        pixel_height = pixels # pixels
        focal_length = 6  # mm
        sensor_width_mm = 6.29  # mm
        sensor_height_mm = 4.71  # mm
        vertical_resolution = 480
        # Calculate the sensor height in millimeters
        sensor_height = (sensor_height_mm * pixel_height) / vertical_resolution
        # Calculate the angular height of the object in radians
        angular_height = m.atan(sensor_height / (2 * focal_length))
        # Calculate the distance to the object in meters or feet
        distance = (object_height / 2) / m.tan(angular_height)
        distance = round(distance, 2)
        distance = distance * 3.3
        return distance

        

#Very rough estimate, Based on a 1.8m tall person/ 6feet
def pixelHeightDistanceAway(pixels):
    # Define the real-world height of the object in meters or feet
    object_height = 1.82  # meters
    pixel_height = pixels # pixels
    focal_length = 6  # mm
    sensor_width_mm = 6.29  # mm
    sensor_height_mm = 4.71  # mm
    vertical_resolution = 480
    # Calculate the sensor height in millimeters
    sensor_height = (sensor_height_mm * pixel_height) / vertical_resolution
    # Calculate the angular height of the object in radians
    angular_height = m.atan(sensor_height / (2 * focal_length))
    # Calculate the distance to the object in meters or feet
    distance = (object_height / 2) / m.tan(angular_height)
    distance = distance * 3.3
    distance = round(distance, 2)
    return distance

def getBboxCentre(bbox):
    return (((bbox[2]-bbox[0])/2 + bbox[0]), (((bbox[3]-bbox[1])/2)+bbox[1]))  


##Dont use
def checkPixelHeight(self,bbox):
        height = bbox[3] - bbox[1]
        if((height > 250 ) & (height < 180)):
            return (True,height)
        else:
            return (False,height)


###Dont use.        
#Parallax Correction for Height
def pHeightRealHeight(pixels):
    theta = cameraAngle
    realPHeight =  pixels * 1/(m.cos(theta) / (1 - m.sin(theta)))
    return realPHeight




#At the distance the person is, theyre the same height, therefore, a perfect lateral shuffle in their plane should be roughly a percent of their height, can use their height for this.
#Returns a estimate based on pixel height of a lateral distance to move
def pixelLateralDistanceEstimation(lateralPixelDistance, pixels)->float:
    return 6 * ((piCameraResolution[1]/pixels)*(lateralPixelDistance/pixels))
    #return(6 * ((pixels - lateralPixelDistance)/(piCameraResolution[1])))-6
    #return (6 *(((pixels / piCameraResolution[1])) * (((pixels / piCameraResolution[1])) * (( piCameraResolution[1]) / (lateralPixelDistance))))
    

#Returns Distance to the Drone from the subject
def distanceToDrone(height):
    return pHeightRealHeight(height) * m.tan(psi)


#Vector from the drone to the subject in meters
#mavLink uses x forward, y to the right, z ascend.
#Should be in 'meters' approximation
def vectorInstruction(bbox)->tuple:
    y = ((bbox[2]-bbox[0])/2 + bbox[0]) - centreScreen[0]
    z =  (((bbox[3]-bbox[1])/2)+bbox[1]) - centreScreen[1]
    return (y,z)


        



        



            
            

        


        
        




        



        
            

        



    
    









