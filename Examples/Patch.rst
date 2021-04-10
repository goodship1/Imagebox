Patch.py
======

Sample based patch Attack

.. code-block:: python 

        from Attacks import Patch
        patch = Patch()
        model = 'pretrained classfier'
        image = 'image file path'
        result = patch.samplebased(image,model)
        
        

Sample based patch RBG Attack
  
.. code-block:: python 
  
   from Imagebox.Attacks import Patch
   
   patch = Patch()
   model = 'pretrained classfier'
   image = 'image file path'
   RBG = (0,0,0)
   results = patch.samplebasedrbg(image,RBG,model)
   print(results[0]) #prints the predcition of the attack
   print(result[1])#prints  the image array
   
   
MPA patch attack with three samples the default implementation wth defualt grey scale 

 
.. code-block:: python 
  
   from Attacks import Patch
   
   patch = Patch()
   model = 'pretrained classfier'
   image = 'image file path'
   greyscale =  True
   samples =  3
   results = patch.MPA(image,model,greyscale,samples)
   print(results[0])#prints the prediction
   print(results[1])#prints the image array
   
   
   
MPA patch attack with three samples the default implementation wth defualt grey scale with no model 
 
 
.. code-block:: python 
  
   from Attacks import Patch
   
   patch = Patch()
   image = 'image file path'
   greyscale =  True
   samples = 3 
   
   result =  patch.MPA(image,model=None,greyscale,samples)
   print(result[0])#prints the image array
   
   
MPA patch attack with three samples the default implementation with greyscale  and custom sample size
  
  
  
.. code-block:: python 
  
   from Attacks import Patch
   
   patch = Patch()
   image = 'image file path'
   greyscale =  True
   samples =  10
   results =  patch.MPA(image,model,greyscale,samples)
   print(results[0])
   print(results[1])
   
  
  
   
   
MPA patch attack with three samples the default implementation without greyscale  and default sample size
  
.. code-block:: python 
    
       from Attacks import Patch
       
       patch = Patch()
       image = 'image file path'
       greyscale =  False
       model = 'pretrained classifer'
       samples = 3 
       result =  patch.MPA(image,greyscale,model,samples)
       
       
HPA patch attack with mutilclassfier neural network.
 
.. code-block:: python 
       
       from Attacks import Patch
       
       patch = Patch()
       image = 'image file path'
       model = 'pretrained classifer'
       classify =  'Multi'
       samples =  3 
       results =  patch.HPA(image,model,classify,samples)
       print(results[0])
       

HPA patch attack with binary neural network.
 

.. code-block:: python 
       
       from Attacks import Patch
 
       patch = Patch()
       image = 'image file path'
       model = 'pretrained classifer'
       classify =  'binary'
       samples = 3 
       
       result  = patch.HPA(image,model,classify,samples)
       print(result[0])#prints the prection
    
 
Adversarial  patch attack.
    
.. code-block:: python 
       
       from Attacks import Patch
       
       patch = Patch()
       image = 'image file path'
       patch = 'image of the patch you wish to apply'
       model = 'your pretrained model'
       result =  patch.adversarialpatch(image,patch,model)
       print(result[0])#prints the prediction of the image
       print(result[1])#prints the image array
       
       
Noise patch 

.. code-block:: python 

        from Attacks import Patch

        patch =  Patch()
        image = 'file path to your image'
        model = 'pretrained nueral network'
        result = patch.noisepatch(image,model)
        print(result[0])#returns the predictiom
        print(result[1])#returns the  image array


       
       
    
    
   
   
  
  
  

   
   

  
