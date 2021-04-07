from PIL import Image, ImageDraw, ImageFilter
import random
import cv2 as cv
from Imagebox.Attacks import Gradcam
class Patch(object):
    '''Class for generating advarsarial patch attack'''

    def __str__(self):
        return "Advarsarial patch's"
    
	def __init__(self):
		self.grad = Gradcam()
   
    def generatepatch(self,image ,rbg = (0,0,0)):
        '''Helper function to generate black patch
        image -> user image
        return -> np.array
        '''
        read =  cv.imread(image)
        width = read.shape[0]
        height =  read.shape[1]
        random_width = random.randint(9,width) - 10
        random_height = random.randint(9,height) - 10
        im = Image.new('RGB',(random_width, random_height), rbg)
        return im


    def samplebasedrbg(self,image,rbg,model = None):
        '''Modfied version of sample based
        image -> image file path
        rbg -> tuple
        return np.array(image)'''
        patch = self.generatepatch(image,rbg)
        image = Image.open(image)
        width = image.size[0]
        height = image.size[1]
        random_width = random.randint(1,width)-1
        random_height = random.randint(1,height)-1
        image.paste(patch,(random_width,random_height))
        if model == None:
			return(image,np.array(image))
        if model != None:
			convert = np.array(image)
			pred = model.predict(convert.reshape(1,image.shape[0],image.shape[1],image.shape[2]))
			return (pred,convert)

    def generatesample(self,image,k):
        '''generate image samples
        image -> user inputted image
        k -> int
        return -> [int]'''
        image = cv.imread(image)
        width = image.shape[0]
        height = image.shape[1]
        sample_set = list()
        for x in range(width):
            for y in range(height):
                    sample_set.append((x,y))
        
        random.shuffle(sample_set)
        index = 0#starting index
        res = [0]*k
        sample_len = len(sample_set)
        for index in range(k):
            res[index] = sample_set[index]
        
        while index < sample_len:
            random_pick = random.randrange(index+1)
            if random_pick < k:
                res[random_pick] = sample_set[index]
            index+=1
        return res

    def HPA(self,image,model=None,classfaction =None,samples =3):
      esp =  self.generatesample(image,samples)
      patch = self.generatepatch(image)
      image = Image.open(image)
      for e in esp:
        image.paste(patch,(e))
      attack_info = (image,np.array(image),esp)
      if model == None:
        return (image,np.array(image),egsp)
      if model != None and classfaction == "binary":
        im =  np.array(image)
        pred = np.argmax(model.predict(im.reshape(1,im.shape[0],im.shape[1],im.shape[2]), axis=-1))
        return (pred,im)
      if model !=None and classfaction == "Multi":
		  im = np.array(image)
		  pred = np.argmax(model.predict(im.reshape(1,im.shape[0],im.shape[1],im.shape[2]) > 0.5).astype("int32"))
		  return (pred,im)
  

    def samplebased(self,image,model=None):
        '''Sample based patch attack gray scale
        image -> user image
        return -> user patch image
        '''
        patch =  self.generatepatch(image)
        image = Image.open(image)
        generate  = random.randint(1,5)
        width , height = image.size
        random_width = random.randint(1,width)
        random_height = random.randint(1,height)
        image.paste(patch,(random_width,random_height))
        if model == None:
				return (image,np.array(image))
        if model != None:
			convert =  np.array(image)
			pred = np.argmax(model.predict(convert.reshape(1,convert.shape[0],convert.shape[1],convert.shape[2])))
			return (pred,convert)
      
    def generatempapatchs(self,image,rbg =(0,0,0)):
        '''Generates the MPA patches of mpa attack
        image -> file path of image
        rbg -> tuple
        return -> image'''
        read = cv.imread(image)
        width = read.shape[0]
        height = read.shape[1]
        random_height =  random.randint(1,height)
        im = Image.new('RGB',(1, random_height), rbg)
        return im
	
    def loadtexture(self):
	    pass
    
    def keyfeatureextraction(self,image):
        pass
        
    def texturepatch(self,image,model):
		pass

    def MPA(self,image,model = None,greyscale = True,samples = 3):
        patch = self.generatempapatches(image)
        esp = self.generatesample(image,samples)
        image = Image.open(image)
        if greyscale == True:
          for e in esp:
            image.paste(patch,(e))
        if greyscale == False:
          rbg =(230,100,50)
          rbg_patch = self.generatempapatch(image,rbg)
          for e  in esp:
            image.paste(patch,(e))
        if model == None and greyscale == True:
          return (image,np.array(image),esp)
        if model != None and greyscale == True:
			convert = np.array(image)
			pred = np.argmax(model.predict(convert.reshape(1,convert.shape[0],convert.shape[1],convert.shape[2])))
			return (pred,convert,esp)
        if model !=None and greyscale == False:
			convert = np.array(image)
			pred = np.argmax(model.predict(convert.reshape(1,convert.shape[0],convert.shape[1],convert.shape[2])))
			return (pred,convert,esp)
			
	def adversarialpatch(self,image,imagetwo,model=None):
		image = Image.open(image)
		imagetwo = Image.open(imagetwo).resize((220,220))
		mask = Image.new("L", image.size, 0)
		draw = ImageDraw.Draw(mask)
		draw.ellipse((20, 20, 130, 130), fill=200)
		new_image = Image.composite(image, imagetwo, mask)
		if model != None:
			convert = np.array(new_image)
			pred = np.argmax(model.predict(convert.reshape(1,convert.shape[0],convert.shape[1],convert.shape[2])))
			return (pred,convert)
		if model == None:
			return new_image
		
          
    
    def gradcamsetup(self,image,model):
        pred = model.predict(image.reshape(1,image.shape[0],image.shape[1],image.shape[2]))
        pred =  np.argmax(pred)
        layers = []
        #for x in range(model.layers):

        
        
