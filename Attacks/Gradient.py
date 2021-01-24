import tensorflow as tf
class Gradient(object):
    '''Gradient class for Gradient based attacks on
    images such as FGSM'''
    def __init__(self):
        self.loss  = None
        self.tape = None

    def __str__(self):
        return "Gradient attacks on images"

    def FGSM(self,image,label):
        '''FGSM attack'''
        pass
