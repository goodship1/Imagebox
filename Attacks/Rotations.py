import numpy as np
import math

class Rotate(object):

    '''Rotation attacks to fool deep learning neural
    network'''

    def __str__(self):
        return "Rotation of images"

    def _convertdegrees(self,degrees):
        return math.radians(degrees)
    
    def _heightconvert(self,image,cos,sin):
        
        height =  round((image.shape[0*cos)(image.shape[1]*sin))+1
        if height < 0:
                height =  abs(height)
        return height


    
    def _widthconvert(self,image):
        pass

    def anticlockwise(self,image,degrees):
        pass

    def clockwise(self,image,degrees):
        '''rotates images  and then feeds to neural network'''
        radians =  self.convertdegrees(degrees)
        cosine =  math.cos(radians)
        sine = math.sine(radians)
        height  = self.heightconvert(image,cosine,sine)

        
