from Imagebox.Attacks import Noise
from Imagebox.Attacks import Contrast
from Imagebox.Attacks import Gradient
from Imagebox.Attacks import Blur
from Imagebox.Attacks import Rotations
import numpy as np
import keras
import PIL
from PIL import Image 

class Training(object):
    
    def __str__(self):
        return "Advarsarial training class"
    
    def __init__(self):
        self.noise = Noise()
        self.contrast = Contrast()
        self.rotate = Rotations()
        self.fgsm = Gradient()
        self.blur = Blur()
        
    
   def writetotrainingpath(self,image,filepath):
        input = input("enter file name")
        image = PIL.Image.fromarray(image, "RGB")
        image.save(input)
        
        
   def contrasttraining(self,image,filepath,model,label):
         pass
   
   def gussianTraining(self,image,filePath,numberofsamples,model,label):
       '''function for generating guassian noise
       images for training'''
        samples_added = 0
        for x in range(numberofsamples):
             gussian_image = self.noise.Gussiannoise(image)
             if np.argmax(model.predict(gussian.image.reshape(1,image.shape[0],image.shape[1],image.shapep[2]))) == label:
                    self.writetotrainingpath(image,file_path)
                    samples_added +=1
         return "number of samples added" + " " + str(samples_added) +" " + "to file path" +" " + filePath
    
                    
             
  
  def randompixelchange(image,label,filepath):
      pass

  def constrasttraining(image,filepath,numberofsamples,levelofcontrast)
      pass

  def saltpeppertraining(self,image,filepath,numberofsamples,model,label):
        '''
        image -> image file path
        filepath -> training absolute file path
        numberofsamples -> total number of noise samples wish to generate
        model -> pretrained classifer
        label -> correct training label
        '''
        samples_added =  0
        for x in numberofsamples:
            speckle_noise =  self.noise.Speckle(image)
            if np.argmax(model.predict(speckle_noise.reshape(1,image.shape[0],image.shape[1],image.shape[2]))) == label:
                self.writetotrainingpath(image,filepath)
                samples_added +=1
        return "number of samples added" + " " + str(samples_added) +" " + "to file path" +" " + filePath
        
        
 def continousclockwise(self,image,filepath,radians,model,label):
    samples = 0
    for x in range(radians):
        self.rotation.clockwise(image,x)
        if np.argmax(model.predict(1,image.shape[0],image.shape[1],image.shape[2]))) == label:
            samples +=1
            self.writetotrainingpath(image,filepath)
    return "number of samples generated" + " " + samples
            

 def rotationtrainingleftsingle(self,image,filepath,radians,model,label):
     '''rotates at sperfic rotation location
        image -> image file path
        filepath -> training file path
        radians -> int
        model -> pretained classfier
        label -> int
        '''
        rot = self.rotations.clockwise(image,radians)
        if np.argmax(model.predict(1,rot.shape[0],rot.shape[1],rot.shape[2]))) == label:
            self.writetotrainingpath(image,filepath)
            
      
        

 def fgsmtraining(image,label,filepath,ep):
     pass
