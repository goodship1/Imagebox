from attacks import noise,constrast

class Training(object):
    
    def __str__(self):
        return "Advarsarial training class"
    
    def __init__(self):
        self.noise = Noise()
        self.contrast = Contrast()
    
   def _gussianfile(image,filepath):
       '''adds gussian noise images to file path'''
       pass

   def _saltpepperfile(image,filepath):
       pass

   def _rotationlefttrainingfile(image,filepath):
       pass

   def _rotationrighttrainingfile(image,filepath):
       pass

   def gussianTraining(image,filePath,numberofsamples):
       '''function for generating guassian noise
       images for training'''
        for x in range(numberofsamples):
             gussian_image = self.noise.Gussian(image)
  
  def randompixelchange(image,label,filepath):
      pass

  def constrasttraining(image,filepath,numberofsamples):
      pass

  def saltpeppertraining(image,filepath,numberofsamples):
      speckle_noise =  self.noise.Speckle(image)

 def rotationtrainingleft(image,filepath,radians):
     '''rotates image'''

 def fgsmtraining(image,label,filepath,ep):
     pass
