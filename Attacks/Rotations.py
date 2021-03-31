import numpy as np
import math

class Rotate(object):

    '''Rotation attacks to fool deep learning neural
    network'''

    def __str__(self):
        return "Rotation of images"

    def convertdegrees(self,degrees):
        return math.radians(degrees)
    
    def heightconvert(self,image,cos,sin):
        
        height =  round((image.shape[0]*cos)+(image.shape[1]*sin))+1
        if height < 0:
                height =  abs(height)
        return height


    
    def widthconvert(self,image,cos,sin):
        width  = round((image.shape[1]*cos)+(image.shape[0]*sin))+1
        if width <0:
                width =  abs(width)
        return width

    def originalwidth(self,image):
        width = round(image.shape[0]+1)
        width = round(width/2)
        return width -1

    def originalheight(self,image):
        height = round(image.shape[1]+1)
        height = round(height/2)
        return height -1

    
    def newcentrewidth(self,width):
        width  = round(width + 1)
        width = round(width /2)
        return width -1

    def newcentreheight(self,height):
        height =  round(height + 1)
        height  = round(height / 2 )
        return height - 1 


    def anticlockwise(self,image,degrees,model=None):
            orginal_x = self.originalwidth(image)
            original_y = self.originalheight(image)
            radians =  self.convertdegrees(degrees)#converts degrees to rads
            cosine =  math.cos(radians)#cosine math function
            sine = math.sin(radians)# sine math function
            height  = self.heightconvert(image,cosine,sine)#calcuates the original height of image
            width =  self.widthconvert(image,cosine,sine)#calcuates the origin height of the image
            center = (orginal_x,original_y)
            convert = (degrees)*-1
            matrix = cv.getRotationMatrix2D(center, convert, scale=1.0)
            rotated = cv.warpAffine(image,matrix, (image.shape[0],image.shape[1]))
            if model == None:
              return rotated
            if model != None:
              pred = np.argmax(model.predict(rotated.reshape(1,image.shape[0],image.shape[1],image.shape[2])))
              return (pred,rotated,degrees)

    def clockwise(self,image,degrees,model = None):
			      
            orginal_x = self.originalwidth(image)
            original_y = self.originalheight(image)
            radians =  self.convertdegrees(degrees)#converts degrees to rads
            cosine =  math.cos(radians)#cosine math function
            sine = math.sin(radians)# sine math function
            height  = self.heightconvert(image,cosine,sine)#calcuates the original height of image
            width =  self.widthconvert(image,cosine,sine)#calcuates the origin height of the image
            center = (orginal_x,original_y)
            matrix = cv.getRotationMatrix2D(center, degrees, scale=1.0)
            rotated = cv.warpAffine(image,matrix, (image.shape[0],image.shape[1]))
            if model == None:
              return rotated
            if model != None:
              pred = np.argmax(model.predict(rotated.reshape(1,image.shape[0],image.shape[1],image.shape[2])))
              return (pred,rotated,degrees)



