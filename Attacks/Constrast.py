import cv2 as cv
import numpy as np
class Contrast(object):
    '''Class for adding constrast to image to reduce to image quality'''
    
    def __str__(self):
        return "functions for adding constrast"
    
    def returnpostive(self,contrast):
        if constrast <0:
            return abs(contrast)
    
    def constrast(self,image,levelofconstrast,model=None):
        if levelofcontrast <0:
            levelofcontrast = self.returnpostive(levelofcontrast)
        alpha = levelofcontrast
        beta = 0
        convertimage = cv.imread(image)
        addconstrast = cv.convertScaleAbs(image,alpha = alpha, beta = beta)
        if model != None:
            covnert_to_numpy = np.array(image)
            pred =  model.predict(image)
            return pred
        elif model == None:
            return addconstrast


