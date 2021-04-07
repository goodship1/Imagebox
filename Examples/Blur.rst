Blur.py
=====

Guassain Blur
=======
..   code-block:: python 
  
 
from Imagebox.Attacks import Blur
  
  blur = Blur()
  stdv =  1 
  kernel_size = (3,3)
  model = 'pretained classifier'
  image = 'image filepath'
  results = blur.guassianblur(stdv,image,kernel_size,model)
  print(results[0])#returns prediction
  print(results[1])#returns image
  print(results[2])#returns standard divation
  print(results[3])#returns kernel size
  
  
  
Average Blur
========
  
.. code-block:: python 
  
  from Imagebox.Attacks import Blur
  
  blur = Blur()
  kernel_size = (3,3)
  model = 'pretained classifier'
  image = 'image filepath'
  results = blur.averageblur(image,kernel_size,model)
  print(results[0])#returns prediction
  print(results[1])#returns image
  
Median Blur
==========

.. code-block:: python 
  
  from Imagebox.Attacks import Blur
  
  blur = Blur()
  percent = 3
  model = 'pretained classifier'
  image = 'image filepath'
  results = blur.medianblur(image,percent,model)
  print(results[0])#returns prediction
  print(results[1])#returns image
  print(results[2])#returns percent

