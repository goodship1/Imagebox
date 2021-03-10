import keras
import numpy as np
import tensorflow as tf

class Gradcam(object):
    
    def __init__(self,model,layername=None,index):
        self.model = model
        self.layername = layername
        self.classindex =  index
    
    def __str__(self):
        return "Grad cam implementation"
    

    def checklayername(self):
        '''
