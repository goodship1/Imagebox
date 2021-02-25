from PIL import Image
import random
import cv2 as cv
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


    def samplebasedrbg(self,image,rbg):
        '''Modfied version of sample based'''
        patch = self.generatepatch(image,rbg)
        image = Image.open(image)
        width = image.size[0]
        height = image.size[1]
        random_width = random.randint(1,width)-1
        random_height = random.randint(1,height)-1
        image.paste(patch,(random_width,random_height))
        return (image,np.array(image))
  

    def generatesample(self,image,k):
        '''generate image samples
        image -> user inputted image'''
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

    def HPA(self,image,model=None,classfaction =None,label = None,samples =3):
      esp =  self.generatesample(image,samples)
      patch = self.generatepatch(image)
      image = Image.open(image)
      for e in esp:
        image.paste(patch,(e))
      attack_info = (image,np.array(image),esp)
      if model == None:
        return (image,np.array(image),esp)
      if model != None and classfaction == "binary":
        im =  np.array(image)
        return np.argmax(model.predict(im), axis=-1)
      if model !=None and classfaction == "Multi":
        return (model.predict(im) > 0.5).astype("int32")

    def samplebased(self,image):
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
        return (image,np.array(image))
      
        
