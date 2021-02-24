from PIL import Image
import random
class Patch(object):
    '''Class for generating advarsarial patch attack'''

    def __str__(self):
        return "Advarsarial patch"
    
   
     def generatepatch(self,image ,rbg = (0,0,0)):
        '''Helper function to generate black patch
        image -> user image
        return -> np.array
        '''
        read =  cv.imread(image)
        width = read.shape[0]
        height =  read.shape[1]
        random_width = random.randint(9,width) - 10
        random_height = random.randint(9,height) - 10
        im = Image.new('RGB',(random_width, random_height), rbg)
        return im


    def samplebasedrbg(self,image,rbg):
        '''Modfied version of sample based'''
        patch = self.generatepatch(image,rbg)
        image = Image.open(image)
        width = image.shape[0]
        height = image.shape[1]
        random_width = random.randint(1,width)-1
        random_height = random.randint(1,height)-1
        image.paste(patch,(random_width,random_height))
        return (image,np.array(image))
  

    

    def samplebased(self,image):
        '''Sample based patch attack gray scale
        image -> user image
        return -> user patch image
        '''
        patch =  self.generatepatch(image)
        image = Image.open(image)
        generate  = random.randint(1,5)
        width , height = image.size
        random_width = random.randint(1,width)
        random_height = random.randint(1,height)
        image.paste(patch,(random_width,random_height))
        return (image,np.array(image))
            
    def generatesample(self,image):
        '''generate image samples
        image -> user inputted image'''
        image = cv.imread(image)
        width = image.shape[0]
        height = image.shape[1]
        sample_set = list()
        for x in range(width):
            for y in range(height):
                    sample_set.append((x,y))
        
        random.shuffle(sample_set)
        k = 3#number of samples generated
        index = 0#starting index
        res = [0]*k
        sample_len = len(sample_set)
        for index in range(k):
            res[index] = sample_set[index]
        
        while index < sample_len:
            random_pick = random.randrange(index+1)
            if random_pick < k:
                res[random_pick] = sample_set[index]
            index+=1
        return res


    def generatenoisepatch(self,image):
        pass

    def noisepatch(self,image):
        pass


    def loadtextures(self):
        pass

    def HPA(self,image,model,label = None):
        epsilion = self.generatesample(image)
        patch = self.generatepatch(Iimage)
        adv = list()
        image = Image.open(image)
        for x in eplison:
            place = image.paste(patch,(x))
            convert =  np.array(place)
            adv.append(convert)
        if label != None:
            for test in adv:
                pred=model.predict(test)
                if pred == label:
                    return 1
        return np.array(adv)





        
    def MPARBG(self,image):
        pass
    
    def TPA(self,image):
        pass

    def texture(self,image):
        pass
    
    def generatepatch(self,model):
        '''Generating advarsarial patch on image'''
        pass
    
    def locationofpatch(self,location):
        '''Location of patch to be applied'''
        pass
        
    def applypatch(self,image):
        '''applying the advarsarial patch of choosen image'''
        pass
