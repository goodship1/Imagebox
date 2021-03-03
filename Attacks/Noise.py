import numpy as np
import cv2 as cv

class Noise(object):
    '''Class for adding different types of
    noise to images'''


    def __str__(self):
        return "A class for adding noise to images"

    def guassian(self,image):
	       image = cv.imread(image)
	       guassian  = np.random.normal(0,mu,image.size)
	       guassian = gussian.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
	       noise_image = cv.add(image,guassian)
	       return noise_image
	       
		

    def gammanoise(self,image):
			image = cv.imread(image)
			gamma = np.random.gamma(100,1,image.size)
			gamma =  gamma.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
			noise_image =  cv.add(image,gamma)
			return noise_image


    def rayleighnoise(self,image):
        	 image =  cv.imread(image)
        	 rayleigh =  np.random.rayleigh(100,image.size)
        	 rayleigh =  rayleigh.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
        	 noise  = cv.add(image,rayleigh)
        	 return noise
    
    def expeontialnoise(self,image):
			image = cv.imread(image)
			exp = np.random.exponential(1,image.size)
			exp = exp.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
			noise =  cv.add(image,exp)
			return noise
    
    def speckle(self,image):
        
        	image = cv.open(image)
        	speckle = np.random(0,1,image.size)
       		speckle = speckle.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
        	image =  image + image
        	noise_image  = image * speckle
        	return noise_image
    
    def possionnoise(self,image):
			image =  cv.open(image)
			pos = np.random.poisson(10,image.size)
			pos = pos.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
			noise =  cv.add(image,pos)
			return noise
		
	      	

   
