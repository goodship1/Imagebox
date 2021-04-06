import pytest
import numpy as np
from Imagebox.Attacks import Noise


class NoiseTests(object):
    
    def __str__(self):
        return "class for containing the various noise attack tests"
    
    def __init__(self):
        self.noise = Noise()
        self.image  = None
        self.label  = None
        self.model =  loadmodel()
        
    def loadmodel(self):
        pass
        
    def GuassianNoisetest(self):
        check = self.noise.gaussian(self.image)
        return assert(check) == type(np.array)
    
    def rayleighnoiseimage(self):
        input = self.image
        check = self.noise.rayleighnoise(input)
        return assert(check) == type(np.array)
    
    def rayleighnoisemode(self):
        input =  self.image
        
        
        
    
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
        


