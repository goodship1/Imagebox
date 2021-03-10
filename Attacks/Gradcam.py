import keras
import numpy as np

class Gradcam(object):

    def __init__(self,model,layername):
        self.model = model
        self.layername = layername

