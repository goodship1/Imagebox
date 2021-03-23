from attacks import noise,constrast

class Training(object):
    
    def __str__(self):
        return "Advarsarial training class"
    
    def __init__(self):
        self.noise = Noise()
        self.contrast = Contrast()
    
   def _gussianfile(self,image,filepath):
       '''adds gussian noise images to file path'''
       pass

   def _saltpepperfile(self,image,filepath):
       pass

   def _rotationlefttrainingfile(image,filepath):
       pass

   def _rotationrighttrainingfile(image,filepath):
       pass

   def gussianTraining(self,image,filePath,numberofsamples,model,label):
       '''function for generating guassian noise
       images for training'''
        samples_added = 0
        for x in range(numberofsamples):
             gussian_image = self.noise.Gussiannoise(image)
             convert =  np.array(gussian_image)
             if model.predict(convert) == label:
                    self.gussianfile(image,file_path)
                    samples_added +=1
         return "number of samples added" + " " + str(samples_added) +" " + "to file path" +" " + filePath
    
                    
             
  
  def randompixelchange(image,label,filepath):
      pass

  def constrasttraining(image,filepath,numberofsamples,levelofcontrast)
      pass

  def saltpeppertraining(self,image,filepath,numberofsamples,model,label):
        samples_added =  0
        for x in numberofsamples:
            speckle_noise =  self.noise.Speckle(image)
            if model.predict(speckle_noise) == label:
                self.speckle_filepath(image,filepath)
                samples_added +=1
        return "number of samples added" + " " + str(samples_added) +" " + "to file path" +" " + filePath
        
        
            

 def rotationtrainingleft(self,image,filepath,radians):
     '''rotates image'''

 def fgsmtraining(image,label,filepath,ep):
     pass
