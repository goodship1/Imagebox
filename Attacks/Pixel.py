import numpy as np
from PIL import image
class Pixel(object):

    '''Class for pixel attacks on images
    The one pixel attack takes  a precoessed image of your choice
    nueral network model of your choice  and the correct label of your
    image'''


    def pixelchange(self,location,image):
        '''changes the pixel at given location
        location -> np.array of pixel change eg (16,16,255,255,255)
        image -> np.array of image
        return  -> np.array of image with pixel change
  
        '''
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
    
    def functionalpixel(self,image,color,changecolor):
        '''Image -> string file path 
           colour -> numpy.array eg (255,255,255)
           changecolor -> numpy.array eg (100,100,100)
           return -> numpy.arry of image
           '''
        read =  Image.open(image)#reads the user inputted image
        width =  read[0]#stores the width of the image
        height = read[1]#stores the height of the image
        for x in range(width):
            for y in range(height):
                current =  read.getpixel((x,y))#reads the current pixel rbg value
                if current == color:#checks if rbg colour is the one to be changed
                    read.putpixel((x,y),colourchange)#changes the pixel
        return np.array(read)

    def onePixel(self,image,label,model):
        '''Applying one pixel change to an image
        image -> image of numpy array format preprocssed
        label -> INT
        model -> trained classfier
        return -> np.array of image
        '''
        height =  image.shape[0]
        widht =  image.shape[1]
        for x in range(width):
            for y in range(height):
                location =  np.array[(x,y,255,255,0])
                makechange = pixelchange(image,location)
                if model.predict_class(image) == label:
                    return makechange
                


                


        



