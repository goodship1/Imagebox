from Attacks.Noise import Noise
from Attacks.Constrast import Contrast
from Attacks.Blur import Blur
from Attacks.Rotations import Rotate
from Attacks.Patch import Patch
from Attacks.Pixel import Pixel
import numpy as np
import keras
import PIL
from PIL import Image
import cv2 as cv 

class Training(object):
    
    def __str__(self):
        return "Advarsarial training class"
    
    def __init__(self):
        self.noise = Noise()
        self.contrast = Contrast()
        self.rotate = Rotate()
        self.blur = Blur()
        self.patch = Patch()
        self.pixel = Pixel()
        
    def contrasttraining(self,image,level,model,label):
       prediction = self.contrast.contrast(image,level,model)
       store = []
       if prediction[0] == label:
         store.append(prediction[1])
       return store

    def gussainnoisetraining(self,image,model,label):
      prediction = self.noise.guassian(image,model)
      store = []
      if prediction[0] == label:
        store.append(prediction[1])
      return store
    
    def raylieghnoisetraining(self,image,model):
      prediction = self.noise.rayleighnoise(image,model)
      store = []
      if prediction[0] == label:
        store.append(prediction[1])
      return store
    
    def gammanoisetrainning(self,image,model):
      prediction = self.noise.gammanoise(image,model)
      store = []
      if prediction[0] == label:
        store.append(prediction[1])
      return store
    
    def expeontialnoisetraining(self,image,model):
     
     prediction = self.noise.expeontialnoise(image,model)
     store = []
     if prediction[0] == label:
       store.append(prediction[1])
     return store

    def speckletraining(self,image,model,label):
      prediciton =  self.noise.speckle(image,model)
      store = []
      if prediction[0] == label:
        store.append(prediction[1])
      return store

    def pixeltraining(self,image,model,samples = 100):
      width = image.shape[0]
      height = image.shape[1]
      store = []
      count = 0
      for x in range(width):
        for y in range(height):
          location = np.array([x,y,255,255,255])
          change = self.pixel.pixelchange(location,image)
          prediction =  np.argmax(model.predict(change.reshape(1,change.shape[0],change.shape[1],change.shape[2])))
          if prediction == label:
            store.append(change)
      return store

      def clockwisetraining(self,image,model,array,label):
        store = []
        for x in range(len(array)):
          prediction  = self.rotation.clockwise(image,array[x],model)
          if prediction[0] == label:
            store.append(prediction[1])

      def anticlockwisetraining(self,image,model,array,label):
        store = []
        for x in range(len(array)):
          prediction =  self.rotation.anticlockwise(image,array[x],model)
          if prediction[0] == label:
            store.append(prediction[1]) 
        return store
      
      def jittertraining(self,image,jitter,model,label):
          store  = []
          for x in range(len(jitter)):
            prediction  = self.pixel.pixeljittering(image,jitter[x],model)
            if prediction[0] == label:
              store.append(prediction[1])
          return store
      
      def shifttraining(self,image,shift,model,label):
        store = []
        for x in range(len(shift)):
          prediction  = self.pixel.pixelshift(image,shift[x],model)
          if prediction[0] == label:
            store.append(prediction[1])
        return store
      
      def samplebasedpatchtraining(self,image,model,label):
        store = []
        prediction  = self.patch.samplebased(image,model)
        if prediction[0] == label:
          store.append(prediction[1])
        return store
      
      def samplebasedcolortraining(self,image,rbg,model,label):
        store = []
        prediction =  self.samplebasedrbg(image,rbg,model)
        if prediction[0] == label:
          store.append(prediction[1])
        return store
      
      def MPATraining(self,image,model,samples,label):
        store = []
        greyscale =  True
        for x in range(len(samples)):
          prediction =  self.patch.MPA(image,model,greyscale,samples[x])
          if prediciton[0] == label:
            store.append(prediction[1])
        return store
      
      def gussianblurtraining(self,image,model,kernel,std,label):
        store = []
        prediction =  self.blur.guassianblur(std,image,kernel,model)
        if prediction[0] == label:
          store.append(prediction[1])
        return store








      


      








    







    




                    
             

