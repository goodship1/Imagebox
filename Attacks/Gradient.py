import tensorflow as tf
import numpy as np
class Gradiant(object):
  """FGSM Attack implemention"""

  def __init__(self):
    self.tape = tf.GradientTape()
    self.loss = tf.keras.losses.CategoricalCrossentropy()
  
  def __str__(self):
    return "Gradient class for the implementation of the gradiant attacks"
  
  def errorhandling(self):
    return " error"

  def FGSM(self,image,label,model):
    """FGSM attack on images"""
    try:
      self.tape.watch(image)#Watches the gradient of input images
      pred = model.predict(image)#Makes the neural network prediction
      loss = self.loss(label,image)#calualtes the loss 
      gradiant = self.tape.gradient(loss, input_image)#calcualtes the gradiant of the image
      signed =  self.tape.sign(gradiant)#calculates the gradaint of image
      return signed
    except:
      print(self.errorhandling())

 def applyfgsm(self,image,esp,label,model):
     signed = self.FGSM(image,label,model)
     results = []
     for x in esp:
        image = image + x * signed
        results.append(image)

    for samples  in results:
        pred = model.predict(samples.reshape(1,samples.shape[0],samples.shape[1],samples.shape[2]))
        if np.argmax(pred) != label:
           return pred



