from enc.encoder import CodewordBuilder
from sympy import *
from common.channel import Channels


class GCC_Encoder:
    inner_codewords=[]

    def __init__(self,field_outer,field_inner,locators,multipliers,staircase_messages):
        self.outer_field=field_outer
        self.inner_field=field_inner
        self.locators=locators
        self.multipliers=multipliers
        self.staircase_messages=staircase_messages


    def encode_outer(self,F,locators,multipliers,messages):
        """GCC_encoder's outer encoder which returns the outer codewords for further encoding. Generated using RS encoder"""
        outer_codewords=[]
        for message in messages:
            encoder=CodewordBuilder(F,message,locators,multipliers)
            codeword=encoder.buildCodeword()
            outer_codewords.append(codeword.c)

        return outer_codewords

    def to_matrix(self,any_array):
        return Matrix(any_array)

    def encode_inner(self,F,locators,multipliers,outer_encoded_message):
        """GCC_encoder's inner encoder which takes each column of outer codewords and encodes into a 2D array using RS encoder"""
        inner_codewords=[]
        inner_messages=[]
        for i in range(0,len(outer_encoded_message[0])):
            msg=[]
            for j in range(0,len(outer_encoded_message)):
                msg.append(outer_encoded_message[j][i])
            inner_messages.append(msg)
        
        for message in inner_messages:
            encoder=CodewordBuilder(F,message,locators,multipliers)
            codeword=encoder.buildCodeword()
            inner_codewords.append(codeword.c)
        return inner_codewords

    def gcc_encoder(self):
        """Build 2D array(Matrix) of GCC codeword
        \nATTENTION: Must be converted to Matrix """
        outer_codewords=self.encode_outer(self.outer_field,self.locators,self.multipliers,self.staircase_messages)
        self.inner_codewords=self.encode_inner(self.inner_field,self.locators,self.multipliers,outer_codewords)

    def get_inner_codewords(self):
        """Return inner_codewords in type of 2d Matrix"""
        self.gcc_encoder()
        return self.inner_codewords


