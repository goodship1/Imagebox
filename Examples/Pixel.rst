
Pixel.py 
==============

Pixel attacks on image attacks include one-pixel RBG jitter targetted one pixel attack , functional pixel attack

One pixel example
==============

..   code-block:: python 

    from Imagebox.Attacks import Pixel
    pixel = Pixel()
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
   file_path = "file path to your image"
   image = cv2.imread(file_path)
   convert =  np.array(image)
   label =  1
   pixel.onePixel(convert,label,model)
   
  
Targetted-One pixel attack example
==============

..   code-block:: python 
        pixel = Pixel()
        target = "different label in your dataset"
        pixel.targettedonepixel(convert,target,model_3)

Functional Pixel Attack
==============

..   code-block:: python 

    pixel = Pixel()
    change = [0,0,0] # color to be change rbg value
    color = [255,255,255]#color to in which change is going to be changed too
    pixel.functionalpixel(image,color,change,model_3)
    
    
    
Pixel jittering Attack
==============

..   code-block:: python 

     pixel =  Pixel()
     jitter = 10
     pixel.pixeljitter(image,jitter,model_3)


    
Pixel shift Attack
==============

..   code-block:: python 
     
     pixel = Pixel()
     shift = 10
     pixel.pixelshift(image,shift,model_3)
     
