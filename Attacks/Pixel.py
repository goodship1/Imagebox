import numpy as np
class Pixel(object):

    '''Class for pixel attacks on images'''
    def imagepreprocessing(image):
        pass
    def pixelchange(image,location):
        store = list()
        location = location.astype(int)
        if location.ndim < 2:
            location = np.array([location])
        for i,image in zip(location,image):
            pixel = np.split(i ,len(i) // 5)
            for x in pixel:
            
    
    def onePixel(image,label,model):
        predictions  = list()
        predictions.append(label)



