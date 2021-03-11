import keras
import numpy as np
import tensorflow as tf
import tensorflow.keras.models as Model
import cv2 as cv
class Gradcam(object):
    
    def __init__(self,model,index,layername=None):
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
        weight = tf.reduce_mean(convert, axis=(0,1))
        cam = tf.reduce_sum(tf.multiply(weights,conv),axis=1)
        (width,height) =(image.shape[2],image.shape[1])
        heat = cv.resize(cam.numpy(),(w,h))
        num = heat - np.min(heat)
        dom = (heat.max() - heatmap.min())+epsilon
        heat = num / dom
        heat = (heat * 255).astype("uint8")
        return heat

    def overlay(self,heat,image,alpha=0.5,color=cv.COLORMAP_VIRDIS):
        heat = cv.applyColorMap(heat,color)
        out = cv.addWeighted(image,alpha,heat,1-alpha,0)
        return(heat,out)













        
