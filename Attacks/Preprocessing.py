import cv2 as cv
import numpy as np
class Preprocessing(object):
    '''Downscale image attacks on image neural netorks'''

    def __str__(self):
        return "Down scaling image attack"


    def downscale(self,imageone,imagetwo,targetshape=(128,128),model = None):
        '''down scaling image attacks
	   imageone -> filepath	
	   imagetwo -> filepath	
	   Target_resizing -> tuple
	   Model -> pretrained classifer'''
        image = cv.imread(imageone)
        target = cv.imread(imagetwo)
        image = cv.resize(target,targetshape)
        if model ! = None:
            merged = np.array(image)
            pred = np.argmax(model.predict(image), axis=-1)
            return pred
        else:
            return image

