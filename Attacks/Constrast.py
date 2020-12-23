import cv2 as cv
class Contrast(object):
    
    def __str__(self):
        return "functions for adding constrast"

    def constrast(image,leveofconstrast):
        alpha = constrast
        beta = 0
        convertimage = cv.imread(image)
        addconstrast = cv.convertScaleAbs(image,alpha = alpha, beta = beta)
        return addconstrast


