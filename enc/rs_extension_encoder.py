import numpy as np
import math
from sympy import *
from common.rs_trial import RSTrial

class RSExtensionFieldEncoder:
    
    def __init__(self,rs_trial):
        """Arguments: field size, message, locators, multipliers, message"""
        self.rs_trial=rs_trial
        self.mod_prime_field = rs_trial.field

    
    def __fetch_generator_array(self,locators, multipliers):
        """Inputs: Locators and multipliers
        :return: Helper function for building the Generator Matrix in 2D array"""
        generator=[]
        for j in range(int(self.rs_trial.message_length)):
            plyM=[]
            for i in range(len(locators)):
                if j==0:
                    plyM.append( self.mod_prime_field(multipliers[i]))
                else:
                    plyM.append(((self.mod_prime_field(locators[i]))**self.mod_prime_field(j))*(self.mod_prime_field(multipliers[i])))
            generator.append(plyM)
        
        print(generator)   
        
        return generator

    def __set_generator_matrix(self,generator):
        """Convert given Array to Matrix type"""
        generatorMatrix=Matrix(generator)
        return generatorMatrix

    def __generate_Trial(self,message,generatorMatrix):
        """Helper function for generating Trial from corresponding inputs"""
        messageVector=Matrix(message).transpose()
        codedMessageNoFF=messageVector*generatorMatrix
        
        encodedMessage=[]
        for i in codedMessageNoFF:
            encodedMessage.append(self.mod_prime_field(i))
    
        return encodedMessage

    def encode(self):
        generator= self.__fetch_generator_array(self.rs_trial.locators,self.rs_trial.multipliers)
        generatorMatrix=self.__set_generator_matrix(generator)
        self.rs_trial.word=self.__generate_Trial(self.rs_trial.message,generatorMatrix)
        


    def get_trial(self):
        """"Builder function to build the Trial"""
        
        self.encode()
        print(self.rs_trial.c)
        return self.rs_trial
    

