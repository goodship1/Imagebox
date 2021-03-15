
Noise.py 
==============

Different types of noise which can added to an image to improve robustness

..   code-block:: python 
        
        ##Gussian Noise added to image
        from Imagebox.Attacks import Noise
        image = cv2.imread(image)
        model =  "Your pretrained classfier"
        label = "label of image for pretrained classfier"
        noise = Noise()# Noise object
        kernel  = (3,3)
        std = 1
        
        Gussian = noise.guassiannoise(image,std,kernel)#Call to gussian Noise without model present returns just the image 
        Gussian noise.gussiannoise(image,std,kernel,model,label)#Gussian noise with model present and label returns the prediction 
        
        ## Gamma noise added to an image example
        gamma = noise.gammanoise(image)# Adds gamma noise to image with both model and label not present will return just noise image
        gamma = noise.gammanoise(image,model,label)#Gamma noise to iamge 
        
        
  
