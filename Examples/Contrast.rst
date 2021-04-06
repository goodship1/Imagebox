Constrast.py
=======


..   code-block:: python 
    
    contrast = Contrast()
    image = 'filepath'
    model =  "your model"
    levelcontrast = 5
    result = contrast.contrast(image,levelofcontrast,model)
    print(result[0])#Prints the prediction to the user
    print(result[1])#Prints np.array of image
    
    
    
