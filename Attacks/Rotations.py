import numpy as np
import math

class Rotate(object):

    '''Rotation attacks to fool deep learning neural
    network'''

    def __str__(self):
        return "Rotation of images"

    def _convertdegrees(self,degrees):
        return math.radians(degrees)
    
    def heightconvert(self,image,cos,sin):
        
        height =  round((image.shape[0*cos)+(image.shape[1]*sin))+1
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

    def imagecheck(self,change_x,change_y,apply_x,apply_y,center_x,center_y,image):
            if 0<= change_x < self.convertwidth(image)
                    and 0<= change_y <=self.convertheight(image)
                    and apply_x >=0 and apply_y>0:
                    return True
            else:
                return False

    def anticlockwise(self,image,degrees):
        pass

    def clockwise(self,image,degrees):
    '''rotates images  and then feeds to neural network'''
        radians =  self.convertdegrees(degrees)#converts degrees to rads
        cosine =  math.cos(radians)#cosine math function
        sine = math.sine(radians)# sine math function
        height  = self.heightconvert(image,cosine,sine)#calcuates the original height of image
        width =  self.widthconvert(image,cosine,sine)#calcuates the origin height of the image
        new_image = np.zeros(height,width,image.shape[2])#creates new image array
        new_height = self.newcentreheight(height)#calcuates the new centre of the orginal image
        new_width =  self.newcentrewidth(width)
        for x in range(height):
            for y in range(height):
                change_x = image.shape[0]-1-x-new_height#changes pixel height of center
                change_y = image.shape[1]-y-new_width#changes pixel width of center
                apply_x = round(-x*sine+y*cosine)#applys the rotation of the image
                apply_y = round(-x*cosine+y*sine)
                center_x = new_width-center_x
                center_y = new_height-center_y
                new_image[center_x,center_y,:] = image[x,y,:]
        return new_image




        
