from setuptools import setup

setup(
	  name = 'Imagebox',
	  version = '1.0',
	  description ='adv machine learning',
	  author ='gavin goodship',
	  packages=['Attacks','Defense'],
	  install_requires=["keras","tensorflow","pytest","cv2","numpy"]
	  )
