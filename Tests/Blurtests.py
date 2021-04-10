 from Attacks import Blur
class Blurtests(object):

    def __init__(self):
        self.image = 'Tests/pablo.jng'
        self.model = None
        self.label = 34
        self.kernel_size = (3,3)
        self.percent = 5
        self.blur =  Blur()

    def gussainblurimage(self):
        result  =self.blur.guassianblur(self.image,self.kernel_size)
        result = type(result)
        assert(result) == type(np.array)
        

    def gussainblurmodel(self):
        result = self.blur.guassianblur(self.image,self.kernel_size ,self.model)
        result = type(result[0])
        assert(result) == type(int)
        
    
    def averageblurimage(self):
        result =  self.blur.averageblur(self.image,self.kernel_size)
        result = type(result)
        assert(result) == type(int)
        
    def averageblurmodel(self):
        result = self.blur.averageblur(self.image,self.kernel_size,self.model)
        result = type(result[0])
        assert(result) == type(int)
        
    def medianblurimage(self):
        result  = self.blur.medianblur(image,percent)
        result = type(result[0])
        assert(result) == type(np.array)

    def medianblurmode(lself):
        pass

    
