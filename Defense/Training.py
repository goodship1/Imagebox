from attacks import noise,constrast

class Training(object):
    
    def __str__(self):
        return "Advarsarial training class"
    
    def __init__(self):
        self.noise = Noise()
        self.contrast = Contrast()
        self.rotate = Rotations()
        self.fgsm = Gradient()
        
    
   def writetotrainingpath(self,image,filepath):
        try:
            

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
            if model.predict(speckle_noise) == label:
                self.speckle_filepath(image,filepath)
                samples_added +=1
        return "number of samples added" + " " + str(samples_added) +" " + "to file path" +" " + filePath
        
        
 def continousclockwise(self,image,filepath,radians,model,label):
    if radians == 360:
        for x in range(1,360):
            images =  self.rotated.clockwie(image,x)
            convert = np.array(images)
            
    for x in radians:
        rotated  = self.rotations.clockwise(image,x)
        convert =  np.array(rotated)
        if model.predict(convert) == label:
            self.writetofilepath(rotated)
            
            

 def rotationtrainingleftsingle(self,image,filepath,radians,model,label):
     '''rotates at sperfic rotation location
        image -> image file path
        filepath -> training file path
        radians -> int
        model -> pretained classfier
        label -> int
        '''
        rotated_image=self.rotate.clockwise(image,radians)
        convert =  np.array(rotated_image)
        if model.predict(convert) == label:
            
            self.writetotrainingpath(image,filepath)
        
        
        

 def fgsmtraining(image,label,filepath,ep):
     pass
