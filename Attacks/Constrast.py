import cv2 as cv
import numpy as np
import keras
class Contrast(object):
    '''Class for adding constrast to image to reduce to image quality'''
    
    def __str__(self):
        return "functions for adding constrast"
    
    def returnpostive(self,contrast):
        if contrast <0:
            return abs(contrast)
    
    def contrast(self,image,levelofcontrast,model=None):
        if levelofcontrast<=0:
            levelofcontrast = self.returnpostive(levelofcontrast)
        alpha = levelofcontrast
        beta = 0
        image = cv.imread(image)
        addcontrast = cv.convertScaleAbs(image,alpha = alpha, beta = beta)
        if model != None:
            pred =  np.argmax(model.predict(addcontrast.reshape(1,image.shape[0],image.shape[1],image.shape[2])))
            return (pred,addcontrast)
        elif model == None:
            return addconstrast
