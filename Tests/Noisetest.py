import pytest
import numpy as np
import keras
from Imagebox.Attacks import Noise


class NoiseTests(object):
    
    def __str__(self):
        return "class for containing the various noise attack tests"
    
    def __init__(self):
        self.noise = Noise()
        self.image  = 'Imagebox/Tests/pablo.jpg'
        self.label  = 34
        self.model =  loadmodel()
        
    def loadmodel(self):
        model_3 = keras.Sequential()
        model_3.add(Conv2D(16,kernel_size =(3,3),input_shape =(300,300,3),activation='relu'))
        model_3.add(MaxPooling2D())
        model_3.add(Conv2D(64,kernel_size =(3,3),activation = 'relu'))
        model_3.add(MaxPooling2D())
        model_3.add(Conv2D(64,kernel_size = (3,3),activation='relu'))
        model_3.add(MaxPooling2D())
        model_3.add(Flatten())
        model_3.add(keras.layers.Dropout(0.5))
        model_3.add(Dense(2000,activation='relu'))
        model_3.add(Dense(51,activation ='softmax'))
        model_3.compile(optimizer='adam',
             loss=tf.keras.losses.categorical_crossentropy,
             metrics=['accuracy']
             )

     model_3.fit(train_gen,validation_data = validation,epochs=10)
     return model_3
        
        
    def GuassianNoisetest(self):
        check = self.noise.gaussian(self.image)
        check = type(check)
        return assert(check) == type(np.array)
    
    def rayleighnoiseimage(self):
        input_image = self.image
        check = self.noise.rayleighnoise(input_image)
        check =  type(check)
        assert(check) == type(np.array)
    
    def rayleighnoisemodel(self):
        input_image =  self.image
        result = self.noise.raylieghnoise(imput_image,self.model)
        result = type(result[0])
        assert(result[0]) == type(int)

    def gammanoiseimagetest(self):
        input_image =  self.image
        result = self.noise.gammanoise(input_image)
        assert(result) == type(np.array)

    def gammanoisemodel(self):
        input_image =  self.image
        result = self.noise.gammanoise(self,image,self.model)
        result = type(result[1])
        assert(result[1]) == type(int)

    def possionnoiseimage(self):
        input_image = self.image
        results =  self.noise.possionnoise(input_image)
        results  = type(results)
        assert(results) == type(np.array)

    def possionnoisemodel(self);
        input_image = self.image
        results =  self.noise.possionnoise(input_image,self.model)
        results = type(results)
        assert(results[0]) == type(int)

    def specklenoiseimage(self):
        results =  self.noise.speckle(self.image)
        results =  type(results)
        assert(results) ==  type(np.array)

    def specklenoisemodel(self):
        results = self.noise.speckle(self.image,self.model)
        results =  type(results)
        assert(results[0]) == type(int)

    def browiannoiseimage(self):
        scale =  1
        mean  = 1
        results = self.noise.browiannoise(self.image,scale,mean)
        results = type(results)
        assert(results) == type(np.array)

    def browiannoisemodel(self):
        scale  = 1 
        mean =  1
        results = self.noise.browiannoise(self.image,scale,mean,self,model)
        results = type(result)
        assert(results) == type(int)

    def expeontialnoiseimage(self):
        results = self.noise.expeontialnoise(self.image)
        results =  type(results)
        assert(results) == type(np.array)



        
        
        
    
    def guassianNoisetest(self,image,label,model):
        pred = self.noise.guassian(image,model,label)
        assert(pred[0]) == type(int) and assert(pred[1]) == type(np.array)

    def gammanoisetest(self,image):
        check = self.noise.gammanoise(image)
        check = type(check)
        assert(check) == type(np.array)

    def gammanoisetest(self,image,model,label):
        result =  self.noise.gammanoise(self.image,self.model,self.label)
        result = type(result[0])
        assert(result) == type(int)

    def raylieghnoise(self):
        result = self.noise.rayleighnoise(self.image)
        result = type(result)
        assert(result) == type(np.array)
    
    def raylieghnoise(self):
        result = self.noise.raylieghnoise(self.image,self.model,self.label)
        result = type(result)
        assert(result) == type(int)

        


