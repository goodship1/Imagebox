import cv2 as cv
class Blur(object):
    '''Class for guassian blur to attack images'''

    def __str__(self):
        return "Gussian blur attack on images"
    

    def guassianblur(stdiv,image,kernel_size):
        '''Function takes an image
        an applies gussian blur to the image
        stakes standard div and image path tuple for kernel size'''
        image = cv.imread(image)
        image =  cv.guassainblur(image,kernel_size,stdiv)
        return image

        
    
