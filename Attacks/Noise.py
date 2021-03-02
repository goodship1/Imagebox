import numpy as np
import cv2 as cv

class Noise(object):
    '''Class for adding different types of
    noise to images'''


    def __str__(self):
        return "A class for adding noise to images"

    def guassian(image):
        '''Adds random guassiannoise to image'''
        image = cv.imread(image)
	mu = 0.5 ** 0.1
        guassian  = np.random.normal(0,mu,image.size)
        guassian = gussian.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
        noise_image = cv.add(image,guassian)
        return noise_image

    def gammanoise(self,image):
	image = cv.imread(image)
	gamma = np.random.gamma(1,1,image.size)
        gamma =  gamma.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')


    def rayleighnoise(self,image):
        pass

    def expeontialnoise(self,image):
        pass
    def speckle(self,image):
        '''Salt and pepper noise
        image -> numpy.array
        return -> noisey image
        '''
        image = cv.open(image)
        speckle = np.random(0,1,image.size)
        speckle = speckle.reshape(image.shape[0].image.shape[1],image.shape[2]).astype('unint8')
        image =  image + image
        noise_image  = image * speckle
        return noise_image

    def possionnoise(self,image):
        pass

