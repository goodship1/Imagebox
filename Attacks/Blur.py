import cv2 as cv
import keras
import numpy as np 
class Blur(object):
    '''Class for  blur  attack images'''

    def __str__(self):
        return "Applies various types of Blurs to iamges"
    
	
	def checkboxfilter(self,box):
		if box[0] % 2!= 0 and box[1] !=0:
			return True
		else:
			return False
	
	def checkpostive(self,percent):
		return percent > 0
	
    def guassianblur(self,stdiv,image,kernel_size,model = None,label= None):
        '''Function takes an image
        an applies gussian blur to the image
        stakes standard div and image path tuple for kernel size'''
        check =  self.checkboxfilter(kernel_size)
        if check == True:
			image = cv.imread(image)
			image =  cv.guassainblur(image,kernel_size,stdiv)
			if model != None and label != None:
					image =  np.array(image)
					pred = np.argmax(model.predict(image), axis=-1)
					return pred
			else:
				return image
			
    def averageblur(self,image,box = (3,3),model = None,label = None):
	   image = cv.imread(image)
	   if self.checkboxfilter(box):
		   average_filter = cv.blur(image,(box[0].box[1]))
		   if model != None and label != None:
			   average_filter = np.array(average_filter)
			   pred = np.argmax(model.predict(average_filter), axis=-1)
			   return pred
		   else:
			   return average_filter
    
    
    def mednblur(self,image,percent,model=None):
		if self.checkpostive(percent):
				image = cv.imread(image)
				median = cv.medianblur(image,percent)
				if model!= None:
					median = np.array(median)
					pred = np.argmax(model.predict(median), axis=-1)
					return pred
				else:
					return median
	
			
		
  
		   
	   
	   

        
    
