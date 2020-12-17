import numpy as np
import cv2 as cv

class Noise(object):
    '''Class for adding different types of
    noise to images'''

    def __str__(self):
        return "A class for adding noise to images"

    def guassian(image):
        '''Adds random guassiannoise to image'''
        image = cv.open(image)
        guassian  = np.random(1,0,image,size)
        guassian = gussian.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
        noise_image = cv.add(image,guassian)
        return noise_image

        

    def speckle(image):
        image = cv.opne(image)
        speckle = np.random(1,0,image.size)
        speckle = speckle.reshape(image.shape[0].image.shape[1],image.shape[2]).astype('unint8')
        noise_image = image * speckle
        return noise_image

