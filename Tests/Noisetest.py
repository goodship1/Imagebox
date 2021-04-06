import pytest
import numpy as np
from Imagebox.Attacks import Noise


class NoiseTests(object):
    
    def __str__(self):
        return "class for containing the various noise attack tests"
    
    def __init__(self):
        self.noise = Noise()
        self.image  = 'Imagebox/Tests/pablo.jpg'
        self.label  = None
        self.model =  loadmodel()
        
    def loadmodel(self):
        pass
        
    def GuassianNoisetest(self):
        check = self.noise.gaussian(self.image)
        return assert(check) == type(np.array)
    
    def rayleighnoiseimage(self):
        input_image = self.image
        check = self.noise.rayleighnoise(input_image)
        assert(check) == type(np.array)
    
    def rayleighnoisemodel(self):
        input_image =  self.image
        result = self.noise.raylieghnoise(imput_image,self.model)
        assert(result[0]) == type(int)

    def gammanoiseimagetest(self):
        input_image =  self.image
        result = self.noise.gammanoise(input_image)
        assert(result) == type(np.array)

    def gammanoisemodel(self):
        input_image =  self.image
        result = self.noise.gammanoise(self,image,self.model)
        assert(result[1]) == type(int)

    def possionnoiseimage(self):
        input_image = self.image
        results =  self.noise.possionnoise(input_image)
        assert(results) == type(np.array)

    def possionnoisemodel(self);
        input_image = self.image
        results =  self.noise.possionnoise(input_image,self.model)
        assert(results[0]) == type(int)

    def specklenoiseimage(self):
        results =  self.noise.speckle(self.image)
        assert(results) ==  type(np.array)

    def specklenoisemodel(self):
        results = self.noise.speckle(self.image,self.model)
        assert(results[0]) == type(int)

    def browiannoiseimage(self):
        results = self.noise.browiannoise(self.image)
        assert(results) == type(np.array)

    def browiannoisemodel(self):

        
        
        
    
    def guassianNoisetest(self,image,label,model):
        pred = self.noise.guassian(image,model,label)
        assert(pred[0]) == type(int) and assert(pred[1]) == type(np.array)

    def gammanoisetest(self,image):
        check = self.noise.gammanoise(image)
        assert(check) == type(np.array)

    def gammanoisetest(self,image,model,label):
        pass

    def rayliegh(self):
        pass
        


