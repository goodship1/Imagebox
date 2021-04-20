import numpy as np
import cv2 as cv
import keras

class Noise(object):
    '''Class for adding different types of
    noise to images'''


    def __str__(self):  
        return "A class for adding noise to images"

    def guassian(self,image,model=None,label=None):
           
	       image = cv.imread(image)
	       guassian  = np.random.normal(0,1,image.size)
	       guassian = guassian.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
	       noise_image = cv.add(image,guassian)
	       if model != None:
			    pred = np.argmax(model.predict(noise_image.reshape(1,image.shape[0],image.shape[1],image.shape[2])))
			    return (pred,noise_image)
	       elif model == None:
			        return noise_image
	       
		

    def gammanoise(self,image,model=None,label=None):
			    image = cv.imread(image)
			    gamma = np.random.gamma(1,1000,image.size)
			    gamma =  gamma.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
			    noise_image =  cv.add(image,gamma)
			    if model != None and label !=None:
				      pred = np.argmax(model.predict(noise_image.reshape(1,image.shape[0],image.shape[1],image.shape[2])), axis=-1)
				      return (pred,noise_image)
			    elif model == None:
				      return noise_image


    def rayleighnoise(self,image,model = None,label=None):
        	 image =  cv.imread(image)
        	 rayleigh =  np.random.rayleigh(100,image.size)
        	 rayleigh =  rayleigh.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
        	 noise  = cv.add(image,rayleigh)
        	 if model != None and label != None:
				        pred = np.argmax(model.predict(noise.reshape(1,image.shape[0],image.shape[1],image.shape[2])))
				        return (pred,noise)
        	 elif model == None:
				        return noise
    
    def expeontialnoise(self,image,model=None,label=None):
			    image = cv.imread(image)
			    exp = np.random.exponential(1000,image.size)
			    exp = exp.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
			    noise =  cv.add(image,exp)
			    if model !=None and label!=None:
				        pred = np.argmax(model.predict(noise.reshape(1,image,shape[0],image.shape[1],image.shape[1])))
				        return (pred,noise)
			    else:
				      return noise
    
    def speckle(self,image,model=None,label=None):
        
        	image = cv.imread(image)
        	speckle = np.random.normal(0,1,image.size)
       		speckle = speckle.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
        	image =  image + image
        	noise_image  = image * speckle
        	if model != None and label != None:
				      pred = np.argmax(model.predict(noise_image.reshape(1,image.shape[0],image.shape[1],image.shape[2])))
				      return (pred,noise_image)
		
    
    def possionnoise(self,image,model =None,label=None):
			  image =  cv.imread(image)
			  pos = np.random.poisson(1000,image.size)
			  pos = pos.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
			  noise =  cv.add(image,pos)
			  if model != None and label!= None:
				    pred = np.argmax(model.predict(noise.reshape(1,image.shape[0],image.shape[1],image.shape[2])), axis=-1)
				    return (pred,noise)
			  elif model == None:
				    return noise
    
    def browiannoise(self,image,scale,mean = 1,model=None,label=None):
                 
                 image = cv.imread(image)
                 browian = np.random.wald(mean,scale,image.size)
                 browian = browian.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
                 noise = cv.add(image,browian)
                 if model!=None and label !=None:
					              pred = np.argmax(model.predict(noise.reshape(1,image.shape[0],image.shape[1],image.shape[2])))
					              return pred
                 elif model == None:
					              return noise
