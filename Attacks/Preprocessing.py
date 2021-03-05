import cv2 as cv
class Preprocessing(object):
    '''Downscale image attacks on image neural netorks'''

    def __str__(self):
        return "Down scaling image attack"


    def downscale(self,imageone,imagetwo,targetshape):
        '''down scaling image attacks'''
        image = cv.imread(imageone)
        image = cv.imread(imagetwo)


