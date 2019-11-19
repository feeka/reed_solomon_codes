from common.extension_field_lut import extension_field
from common.prime_field import prime_field
from common.trial import Trial
#from common.lookup_tables import LookupTablesForGaloisField

class RSTrial(Trial):
    message = []
    generatorMatrix=[]
    c=[]
    multipliers=[]
    locators=[]
    polyview=[]

    def __init__(self,field,msg_length,word_length,locators,multipliers,message=[],word=[],degree=0,polynom=[]):
        """Arguments: field, locators, multipliers, message itself"""
        self.message=message
        self.degree = degree
        self.field=field
        if (word!=[]):
            self.word = word    
        self.multipliers=multipliers
        self.locators=locators
        self.word_length=len(locators)
        self.message_length=msg_length
    

    
