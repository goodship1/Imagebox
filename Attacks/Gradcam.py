import keras
import numpy as np
import tensorflow as tf
import tensorflow.keras.models import Model

class Gradcam(object):
    
    def __init__(self,model,layername=None,index):
        self.model = model
        self.layername = layername
        self.classindex =  index
        self.tape = tf.GradientTape()
        if self.checklayername == None:
            self.getlastlayer()
    
    def __str__(self):
        return "Grad cam implementation"
    
    def layererrorhandling(self):
        return "can not find 4D space"

    def layernumbercheck(self,layers):
        return len(layers) ==4

    def checklayername(self):
        '''check if layer is not none'''
        return self.layername == None

    def getlastlayer(self):
        '''Finding the last layer'''
        reverse =  reversed(self.model.layers)#revesers
        for layer in reverse:
            if self.layernumbercheck(layer.output_shape) == True:
                return layer.name
            else:
                print(self.layererrorhandling())
    
    def heatmap(self,image,epsilon = 1e-8):
        inputs = [self.model.inputs]
        output_1= self.model.get_layer(self.layername).output
        output_2 = self.model.output
        grad = Model(inputs,output_1,output_2)
        with self.tape  as tape:
            inputs = tf.cast(image,tf.float32)
            (conv,pred) = grad(inputs)
            loss = pred[:,tf.argmax(pred[0])]
        gradient = tape.gradient(loss,conv)
        convcast = tf.cast(conv >0,"float32")
        gradcast = tf.cast(grad>0,"float32")
        convert = convcast * castgrad * grad
        conv = conv[0]
        convert = convert[0]









        
