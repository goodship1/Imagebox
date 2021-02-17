import Pixel
from PIL import Image
import random
class Patch(object):
    '''Class for generating advarsarial patch attack'''

    def __str__(self):
        return "Advarsarial patch"
    
    def __init__(self):
        self.pixel  = Pixel()
        #self.gradient = Gradient()
   
    def generateblackpatch(self,image):
        '''Helper function to generate black patch
        image -> user image
        return -> np.array
        '''
        black = (0,0,0)
        read =  cv.imread(image)
        width = image.shape[0]
        height =  image.shape[1]
        random_width = random.randint(width) - 10
        random_height = radom.randint(height) - 10
        im = Image.new('RGB', (random_width, random_height), black)
        return im

    
    def samplebased(self,image):
        '''Sample based patch attack
        image -> user image
        return -> user patch image
        '''
        patch =  self.generateblackpatch(image)
        image = Image.open(image)
        generate  = random.randint(1,5)
        width = image.shape[0]
        height = image.shape[1]
        random_width = random.randint(1,width)
        random_height = random.rand(1,height)
        modified = image.paste((patch,(random_width,random_height)))
        return modified 

            


    def loadtextures(self):
        pass

    def HPA(self,image):
        pass
    def MPA(self,image):
        pass
    
    def TPA(self,image):
        pass

    def texture(self,image):
        pass
    
    def generatepatch(self,model):
        '''Generating advarsarial patch on image'''
        pass
    
    def locationofpatch(self,location):
        '''Location of patch to be applied'''
        pass
        
    def applypatch(self,image):
        '''applying the advarsarial patch of choosen image'''
        pass
