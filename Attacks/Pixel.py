import numpy as np
class Pixel(object):

    '''Class for pixel attacks on images
    The one pixel attack takes  a precoessed image of your choice
    nueral network model of your choice  and the correct label of your
    image'''


    def pixelchange(self,location,image):
        '''changes the pixel at given location'''
        if locations.ndim < 2:
            locations = np.array([locations])
        tile = [len(locations)] + [1]*(locations.ndim+1)
        imgs = np.tile(image, tile)
        locations = locations.astype(int)
    for x,image in zip(locations, imgs):
        pixels = np.split(x, len(x) // 5)
        for pixel in pixels:
            x_pos, y_pos, *rgb = pixel
            image[x_pos, y_pos] = rgb
    
    return imgs
    
    def functionalpixel(self,image,location):
        pass

    def onePixel(self,image,label,model):
        '''Applying one pixel change'''
        height =  image.shape[0]
        widht =  image.shape[1]
        for x in range(width):
            for y in range(height):
                location =  np.array[(x,y,255,255,0])
                makechange = pixelchange(image,location)
                if model.predict_class(image) == label:
                    return makechange
                


                


        



