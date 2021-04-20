from PIL import Image, ImageDraw, ImageFilter
import random
import cv2 as cv
from Attacks.Gradcam import Gradcam
import numpy as np

class Patch(object):
    '''Class for generating advarsarial patch attack'''

    def __str__(self):
        return "Advarsarial patch's"
    
   
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

    def generatenoisepatch(self,image):
        image = cv.imread(image)
        width = image.shape[0]
        height = image.shape[1]
        speckle = np.random.normal(0,1,image.size)
        speckle = speckle.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
        image =  image + image
        image = image * speckle
        rand_h =  random.randint(1,height)
        rand_w = random.randint(1,width)
        im = Image.new('RGB',(rand_h,rand_w))
        return im


    def noisepatch(self,image,model=None):
        noise_patch = self.generatenoisepatch(image)
        image = Image.open(image)
        file_path = 'Attacks/noise12.png'
        image_two = Image.open(file_path).resize(image.size)
        width,height =  image.size
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        ran = random.randint(1,10)
        ran_1 = random.randint(1,10)
        draw.ellipse((ran, ran_1, 20, 20), fill=200)
        new_image = Image.composite(image_two,image, mask)
        if model !=None:
            convert =  np.array(new_image)
            pred = model.predict(convert.reshape(1,convert.shape[0],convert[1],convert.shape[2]))
            return (pred,convert)

        if model == None:
            return new_image



    def loadtexture(self):
	    file_path = 'Attacks/saving.jpeg'
	    return file_path
    
    def keyfeatureextraction(self,image):
        return image
        
    def texturepatch(self,image,model=None):
      image = Image.open(image)
      width,height  = image.size
      texture =  self.loadtexture()
      imagetwo = Image.open(texture).resize(image.size)
      mask = Image.new("L", image.size, 1)
      draw = ImageDraw.Draw(mask)
      ran = random.randint(1,100)
      ra =  random.randint(1,100)
      draw.rectangle((ran, ra, 90, 90), fill=300)
      new_image = Image.composite(imagetwo,image ,mask)
      if model != None:
        convert = np.array(new_image)
        pred = np.argmax(model.predict(convert.reshape(1,convert.shape[0],convert.shape[1],convert.shape[2])))
        return (pred,convert)
      if model == None:
        return new_image
		

    def MPA(self,image,model = None,greyscale = True,samples = 3):
        patch = self.generatempapatchs(image)
        esp = self.generatesample(image,samples)
        image = Image.open(image)
        if greyscale == True:
          for e in esp:
            image.paste(patch,(e))
        if greyscale == False:
          rbg =(230,100,50)
          rbg_patch = self.generatempapatchs(image,rbg)
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

		
          
    
    def gradcamsetup(self,image,model):
        image = cv.imread(image)
        pred = model.predict(image.reshape(1,image.shape[0],image.shape[1],image.shape[2]))
        pred =  np.argmax(pred)
        layers = []
        for x in(len(model.layers)):
            layer = (model.get_layer(index = x).name)
            layers.append(layers)
        grad = Gradcam(model,pred,layers[2])
        grad  = grad.compute_heatmap(image.reshape(1,image.shape[0],image.shape[1],image.shape[2]))
        return grad
    def adversarialpatch(self,image,imagetwo,model=None):
      image = Image.open(image)
      imagetwo = Image.open(imagetwo).resize((image.size))
      mask = Image.new("L", image.size, 0)
      draw = ImageDraw.Draw(mask)
      ran_1 = random.randint(1,10)
      ran_2 = random.randint(1,10)
      draw.ellipse((ran_1,ran_2, 130, 130), fill=200)
      new_image = Image.composite(image, imagetwo, mask)
      if model != None:
        convert = np.array(new_image)
        pred = np.argmax(model.predict(convert.reshape(1,convert.shape[0],convert.shape[1],convert.shape[2])))
        return (pred,convert)
      if model == None:
        return new_image

        
        

