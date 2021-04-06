Rotations.py
=======

Clockwise rotation
========
..   code-block:: python 

  from Imagebox.Attacks import Rotate
  
  model = 'Your pretained classfier'
  degrees =  45
  image = 'image file path'
  
  rotate = Rotate()
  results  = rotate.clockwise(image,degrees,model)
  print(results[0])#returns the predicton
  print(results[1])#returns the np.array of the rotated image
  print(results[2])#returns the degrees which have been rotated
  
  
anti-clockwise rotation
========

..   code-block:: python 

  from Imagebox.Attacks import Rotate
  
  model = 'Your pretained classfier'
  degrees =  45
  image = 'image file path'
  
  rotate = Rotate()
  results  = rotate.anticlockwise(image,degrees,model)
  print(results[0])#returns the predicton
  print(results[1])#returns the np.array of the rotated image
  print(results[2])#returns the degrees which have been rotated
