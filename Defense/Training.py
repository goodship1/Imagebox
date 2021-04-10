from Attacks import Noise
from Attacks import Contrast
from Attacks import Gradient
from Attacks import Blur
from Attacks import Rotations
from Attacks import Patch
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
        file_name = input("enter file name")
        image = PIL.Image.fromarray(image, "RGB")
        path  =  file_path + '/'+file_name
        Image.save(path)

        
    
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

  def constrasttraining(image,filepath,levelofcontrast,model,label)
      cons =  self.constrast.contrast(image,levelofcontrast,model)
      pred =  cons[0]
      if pred == label:
            self.writetotrainingpath(image,filepath)
            return "sample added"
            
      

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
    
 
 def samplebasedtraining(self,image,filepath,model,label,samples):
     for x in range(samples):  
        result = self.patch.samplebased(image,model)
        pred = result[0]
        
  
     

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
