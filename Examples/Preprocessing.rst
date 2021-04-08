Preprocessing.py
=========

Downsampling image attack with default parameters overidden.

..   code-block:: python 
    
    from Imagebox.Attacks import Preprocessing
    
    pre = Preprocessing()
    image_one = 'first file image"
    image_two = 'scond file image"
    target_size = 'your network input shape'
    model = 'Your pretrained classifer'
    results =  pre.downsampling(image_one,image_two,target_size,model)
    print(results[0])#Returns the prediction of the neural network
    print(results[1])#Returns the imageone
    print(results[2])#returns the image two
    
Preprocessing.py
=========

Downsampling Attack with no pretrained classfier.Returns the numpy array of down sampled image 

..   code-block:: python 

  from Imagebox.Attacks import Preprocessing
  pre = Preprocessing()
  image_one = 'first file image"
  image_two = 'scond file image"
  target_size = 'your target size of input layer'
  results = pre.downsampling(image_one,image_two,target_size)
  

