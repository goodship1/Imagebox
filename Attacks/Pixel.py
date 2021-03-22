import numpy as np
from PIL import Image
class Pixel(object):

    '''Class for pixel attacks on images
    The one pixel attack takes  a precoessed image of your choice
    nueral network model of your choice  and the correct label of your
    image'''


    def pixelchange(self,locations,image):
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
        for x,image in zip(locations ,imgs):
            pixels = np.split(x, len(x) // 5)
            for pixel in pixels:
                x_pos, y_pos, rgb = pixel
                image[x_pos, y_pos] = rgb
        return imgs
  
    
    def functionalpixel(self,image,color,changecolor,model= None):
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
        height =  image.shape[1]
        widht =  image.shape[0]
        for x in range(width):
            for y in range(height):
                location =  np.array([x,y,255,255,0])
                makechange = self.pixelchange(image,location)
                if model.predict_class(makechange) != label:
                    return makechange
                
	def targetedpixel(self,image,model,target):
		'''applying targetted pixel attack
		image -> numpy array
		model -> pretrained classifer
		target -> label of target '''
		height = image.shape[1]
		width = image.shape[0]
		for x in range(width):
			for y in range(width):
				location = np.array([x,y,255,255,0])
				change  = self.pixelchange(image,location)
				if model.predict_class(image) == target:
					return change

        

        def pixeljittering(self,image,jitter,shift = None,model=None,label=None):
            '''Image -> file path
               jitter -> int
               model -> pre-trained classfier
               label -> int
            '''
            if shift == None:
                 image = cv.imread(image)
                 width = image.shape[0]
                 height = image.shape[1]
                 colour =  image.shape[2]
                 noise = np.random.randint(0,jitter,(width,height))
                 zeros = np.zeros_like(image)
                 zeros[:,:,1] = noise
                 add =  cv.add(image,noise)
                 if model == None  and label == None:
                     return add
                 elif model != None:
                     convert =  np.array(add)
                     pred  = model.predict(convert)
                     return pred
            if shift!=None:
                    image = cv.imread(image)
                    red = image[:,:,0]
                    blue = image[:,;,1]
                    green = image[:,;,2]
                    shift_r = np.roll(red,shift,axis=0)
                    shift_g = np.roll(green,shift,axis=1)
                    shift_b = np.roll(blue,shift,axis = 0)
                    pixel_shift = np.dstack((shift_r,shift_g,shift_b))
                    if model == None:
                        return pixel_shift
                    elif model != None:
                        convert = np.array(pixel_shift)
                        pred = model.predict(convert)
                        return pred




                









