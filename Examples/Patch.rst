Patch.py
======

Sample based patch Attack

.. code-block:: python 

        from Imagebox.Attacks import Patch
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
  
   from Imagebox.Attacks import Patch
   
   patch = Patch()
   model = 'pretrained classfier'
   image = 'image file path'
   greyscale =  True
   samples =  3
   results = patch.MPA(image,model,greyscale,samples)
   print(results[0])#prints the prediction
   print(results[1])#prints the image array
   
   
   
  

   
   

  
