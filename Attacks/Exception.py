import Exception
class Error(Exception):
    

    def __str__(self):
        return "Error string"

    def FGSMerror(self):
        return "FGSM cant be applied"
