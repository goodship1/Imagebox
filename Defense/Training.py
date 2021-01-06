from attacks import noise

class Training(object):
    
    def __str__(self):
        return "Advarsarial training class"
    
    def __init__(self):
        self.noise = Noise()
    
   def _gussianfile(image,filepath):
       '''adds gussian noise images to file path'''
       pass
   def gussianTraining(image,filePath,numberofsamples):
       '''function for generating guassian noise
       images for training'''
        for x in range(numberofsamples):
             gussian_image = self.noise.Gussian(image)
  
  def saltpeppertraining(image,filepath,numberofsamples):
      speckle_noise =  self.noise.Speckle(image)

