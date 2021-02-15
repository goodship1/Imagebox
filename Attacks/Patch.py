import keras

class Patch(object):
    '''Class for generating advarsarial patch attack'''

    def __str__(self):
        return "Advarsarial patch"
        
    def MPA(self,image):
        pass
    
    def TPA(self,image):
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
