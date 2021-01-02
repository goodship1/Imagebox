import cv2 as cv
class Contrast(object):
    '''Class for adding constrast to image to reduce to image quality'''
    
    def __str__(self):
        return "functions for adding constrast"

    def constrast(self,image,levelofconstrast):
        alpha = constrast
        beta = 0
        convertimage = cv.imread(image)
        addconstrast = cv.convertScaleAbs(image,alpha = alpha, beta = beta)
        return addconstrast


