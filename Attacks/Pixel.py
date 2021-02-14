import numpy as np
class Pixel(object):

    '''Class for pixel attacks on images'''


    
    
    def functionalpixel(self,image,location):
        pass

    def onePixel(self,image,label,model):
        '''Applying one pixel change'''
        image = cv.read(image)
        width,height =  image.shape
        for x in range(width):
            for y in range(height):
                location =  np.array[(x,y,255,255,0])
                makechange = pixelchange(image,location)
                if model.predict_class(image) == label:
                    return makechange
                elif modle.predict_class(image) != label:
                     image = cv.read(image)



                


        



