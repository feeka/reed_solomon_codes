# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 21:48:34 2018

@author: Fikrat Talibli
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is an original decoder for analysis of GC codes for DNA fields.
"""
import types

import numpy as np
import math
from common.trial import Trial
from math import fabs
from common.prime_field import prime_field
from sympy import *

class RSPrimeDecoder:
    """
    A class used to represent a Decoder with 
    corresponding attributes and methods described below.
    ...
    Constructor:
    field_size: int
        represents size of prime field
    locators: int[]
        represents the integer list where locators are stored
    multipliers: int[]
        represents the integer list where multipliers are stored
    received_codeword: int[]
        represents the integer list where received codeword is stored
    msg_size: int[]
        representation of message size 

    Attributes
    ----------
    codeword: Codeword
        represents codeword see @codeword
    
    Methods
    -------
    interpolate_points(locators, received_codeword)
        method to represent interpolation points, acts as a helper for user
    
    calculate_polynoms(degQ0,degQ1,locators)
        calculates the corresponding

    multiply_using_polynom(c1,c2)
        takes two int[] arguments
        used as a helper methods for multiplying two polynomials
    
    
    """

    interpolation_points=[]
    deg_Q0=[]
    deg_Q1=[]

    msg_size=0
    def __init__(self,trial):
        #self.=Codeword(field_size,locators,multipliers,received_codeword=receivedCodeWord)
        self.trial  = trial
        self.msg_size=trial.message_length
        self.codeword_length=trial.word_length
        self.deg_Q0=self.codeword_length-(math.floor((self.codeword_length-self.msg_size)/2))-1
        self.deg_Q1=math.ceil((self.codeword_length-self.msg_size)/2)
        self.locators = trial.locators
        self.field_size = trial.field.p
        self.received_codeword = trial.word
        self.mod_field_size=prime_field(self.field_size)
        #self.field_size = self.trial.field
    
    def get_interpolate_points(self,locators,receivedWord):
        """Returns interpolation points"""
        count=[]
        interpolationTuple=[]

        for i in locators:
            tempArray=[]
            tempArray.append(i)
            tempArray.append((self.trial.word[count]))
            interpolationTuple.append(tempArray)
            count+=1
        
        return interpolationTuple
    
    def __calculate_polynoms(self,degQ0,degQ1,locators):
        """Inputs: degQ0 and degQ1
        Output: Matrix type vector with """
        
        rows1=[]
        rows2=[]
        
        
        #since we have 2 polynoms in reality => there are really 2 logically separated
        #coefficients delimited by degrees of corresponding polynoms in the returned vector
        n = (self.codeword_length)
        for i in range(0,n):
            tempArray=[]
            for j in range(0,degQ0+1):
                tempArray.append(self.trial.field((locators[i]**j)))
            rows1.append(tempArray)
        
        for i in range(0,n):
            tempArray=[]
            for j in range(0,degQ1+1):
                tempArray.append(self.trial.field(locators[i]**j)*self.trial.word[i])
            rows2.append(tempArray)
        resultedRows=[]
        for m in range(0,n):
            resultedRows.append(rows1[m]+rows2[m])
        return resultedRows
    
    def __add_minus_one(self,length,element_index):
        """Fills the array of length l-1 elements with zeros; and adds -1 in one of positions
        :return:  returns array of 0's with length l with -1 at element_index"""
        array_to_return=[]
        """localFF=self.ff"""
        for i in range(0,length):
            array_to_return.append(self.trial.field(0))
            if i==element_index:
                array_to_return[i]=self.trial.field(-1)
        return array_to_return
    
    def __calculate_coefficients(self, res_row):
        """Calculates coefficients for each polynom returns result wrapped in 1 array -1 trick is also covered below
        :return: array of polynom elements
        """
        self.__to_reduced_row_echelon_form(res_row)
        all_zero_row = [self.trial.field(0)]*len(res_row[0])
        rm_indexes = []
        count = len(res_row)-1
        c1=0
        while count>=0:
            if res_row[count] == all_zero_row:
                c1+=1
                if c1>=1 :
                    del(res_row[count])
                    count = count-1
                    continue
                if count==len(res_row):
                    count = count - 1
                
            count=count-1
        
        if len(res_row)!=len(res_row[0]):
            count=len(res_row[0])
            for i in range(0,count):
               
                if i!=len(res_row[0])-1:
                    if len(res_row)-1>=i:
                        if res_row[i][i]!=self.trial.field(1):
                            
                            colT=self.__add_minus_one(len(res_row[0]),i)
                            res_row.insert(i,colT)
                            

                        else:
                            continue
                    else:
                        if(len(rm_indexes)!=0  and res_row[i-1][i-1]==self.trial.field(-1)):
                                rm_indexes.remove(i)
                        colT=self.__add_minus_one(len(res_row[0]),i)
                        res_row.insert(i,colT)
                        rm_indexes.append(i+1)
                else:
                    colT=self.__add_minus_one(len(res_row[0]),i)
                    res_row.insert(i+1,colT)
                    rm_indexes.append(i+1)
                    break
        count=0
        polynomElems=[]
        for elements in res_row:
            for i in range(0,len(elements)):
                if i == len(elements)-1:
                    polynomElems.append((elements[i]))
        i = 0
        return polynomElems
    
    def __to_reduced_row_echelon_form(self, M):
        if not M: return
        lead = 0
        rowCount = len(M)
        columnCount = len(M[0])
        for r in range(rowCount):
            if lead >= columnCount:
                return
            i = r
            while M[i][lead] == self.trial.field(0):
                i += 1
                if i == rowCount:
                    i = r
                    lead += 1
                    if columnCount == lead:
                        return
            M[i],M[r] = M[r],M[i]
            lv = M[r][lead]
            M[r] = [ mrx / lv for mrx in M[r]]
            for i in range(rowCount):
                if i != r:
                    lv = M[i][lead]
                    M[i] = [ (iv -lv*rv) for rv,iv in zip(M[r],M[i])]
            lead += 1
    

    def __divide_polynoms(self,polynomElems):
        
        count=0
        q0Elements=[]
        q1Elements=[]
        
        if self.trial.word_length != (len(polynomElems)-2):
            count = len(polynomElems) -self.trial.word_length- 2 
        for i in range(0,self.deg_Q0+1):
            q0Elements.append(polynomElems[i]*self.trial.field(-1))
        for i in range(self.deg_Q0+1,len(polynomElems)):
            q1Elements.append(polynomElems[i])


        q0Elements.reverse()
        q1Elements.reverse()
        longDivRes=self.__extended_synthetic_division(q0Elements, q1Elements)[0]
        longDivRes.reverse()
        return list(longDivRes)


    def __extended_synthetic_division(self,dividend, divisor):
        '''Fast polynomial division by using Extended Synthetic Division. Also works with non-monic polynomials.'''
        # dividend and divisor are both polynomials, which are here simply lists of coefficients. Eg: x^2 + 3x + 5 will be represented as [1, 3, 5]
    
        out = list(dividend) # Copy the dividend
        normalizer = divisor[0]
        for i in range(len(dividend)-(len(divisor)-1)):
            out[i] /= normalizer # for general polynomial division (when polynomials are non-monic),
                                     # we need to normalize by dividing the coefficient with the divisor's first coefficient
            coef = out[i]
            if coef != 0: # useless to multiply if coef is 0
                for j in range(1, len(divisor)): # in synthetic division, we always skip the first coefficient of the divisor,
                                                  # because it's only used to normalize the dividend coefficients
                    if isinstance(divisor[j], int): 
                        out[i + j] += self.trial.field(-1)*self.trial.field(divisor[j]) * coef
                    else: out[i + j] += self.trial.field(-1)*(divisor[j]) * coef
                    
    
        # The resulting out contains both the quotient and the remainder, the remainder being the size of the divisor (the remainder
        # has necessarily the same degree as the divisor since it's what we couldn't divide from the dividend), so we compute the index
        # where this separation is, and return the quotient and remainder.
        separator = -(len(divisor)-1)
        return out[:separator], out[separator:] # return quotient, remainder.


    def __decode_codeword(self):
        """ Decode codeword R to C """
        resultedRows=self.__calculate_polynoms(self.deg_Q0,self.deg_Q1,self.trial.locators)
        polynomElems=self.__calculate_coefficients(resultedRows)
        polynomCoefficients=self.__divide_polynoms(polynomElems)
        self.trial.message=polynomCoefficients

    def decode(self):
        self.__decode_codeword()
