import numpy as np
import keras 
class Pixel(object):

    '''Class for pixel attacks on images'''


    def pixelchange(image,location):
        '''Changing pixel at current location'''
        store = list()
        location = location.astype(int)
        if location.ndim < 2:
            location = np.array([location])
        for i,image in zip(location,image):
            pixel = np.split(i ,len(i) // 5)
            for x in pixel:
                x_pos ,y_pos * rgb = x
                image[x_pos,y_pos] = rgb
        return image
    
    def onePixel(image,label,model):
        '''Applying one pixel change'''
        image = cv.read(image)
        width,height =  image.shape

        predictions  = list()
        pixel_list = list()
        predictions.append(label)
        



