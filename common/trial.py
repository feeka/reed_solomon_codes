from common.extension_field_lut import extension_field
from common.prime_field import prime_field
#from common.lookup_tables import LookupTablesForGaloisField

class Trial:
    message = []
    generatorMatrix=[]
    c=[]
    multipliers=[]
    locators=[]
    polyview=[]

    def __init__(self,fieldSize,locators,multipliers,message=[],word=[],degree=0,polynom=[]):
        """Arguments: field, locators, multipliers, message itself"""
        self.message=message
        self.degree = degree
        if (degree!=0):
            self.field=extension_field(fieldSize,degree,polynom)
        elif(degree==0):
            self.field=prime_field(fieldSize)
        if (word!=[]):
            self.word = word       

    
    

    def get_codeword(self):
        """Return codeword in array type"""
        return self.c

    def get_message(self):
        """Return message in array type"""
        return self.message
    
    def get_multipliers(self):
        """Return multipliers in array type"""
        return self.multipliers
    
    def get_locators(self):
        """Return locators in array type"""
        return self.locators

    def get_generatorMatrix(self):
        """Return generator matrix in array type"""
        return self.generatorMatrix    
    