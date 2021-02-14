import error as e
import tensorflow as tf
class Gradiant(object):
  """FGSM Attack implemention"""

  def __init__(self):
    self.tape = tf.GradientTape()
    self.loss = tf.keras.losses.CategoricalCrossentropy()
    self.error =  Error()
  
  def __str__(self):
    return "Gradient class for the implementation of the gradiant attacks"
  
  def errorhandling(self):
    return self.error.FGSMerror()

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

