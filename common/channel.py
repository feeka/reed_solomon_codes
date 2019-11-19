import numpy as np
import math
import random


class Channel:
    
    
    def apply_DMC_channel(self,rs_trial,p=0):
        self.rs_trial = rs_trial
        field = [self.rs_trial.field(num) for num in range((rs_trial.field.p))]
        self.rs_trial.message=[] 
        self.quantity_of_positions_distorted = 0
        for i in range(len(rs_trial.word)):
            s=random.uniform(0,1)
            if (s<p):
                self.quantity_of_positions_distorted+=1
                temp =random.choice(field) 
                del(self.rs_trial.word[i])
                self.rs_trial.word.insert(i,temp)
            else:
                continue

    def error_for_gcc_channel(self,fieldSize,probabilityError,n_inner,k_inner):
        """Input: field size, probability of an error, n_inner, k_inner; 
        \nOutput: array typed error matrix
        \nAttention: please consider converting to Matrix for usage as a matrix"""
        self.fieldSize=fieldSize
        field=[]
        for i in range(0,fieldSize):
            field.append(i)
        E_array=[]
        for i in range(0,n_inner):
            innerarray=[]
            for j in range(0,k_inner):
                s = random.uniform(0, 1)
                if (s<probabilityError):
                    innerarray.append(random.choice(field)%fieldSize)
                elif (s>=probabilityError):
                    innerarray.append(0)
            E_array.append(innerarray)
        return E_array
    
    def get_noisy_vector(self,C,E):
        """Input: Codeword in 2D Array, E Matrix in 2D Array 
        \n Output: Distorted 2D Array"""
        R=[]
        for i in range(0,len(E)):
            result=[]
            for j in range(0,len(E[0])):
                result.append((C[i][j]+E[i][j])%self.fieldSize)
            R.append(result)
        return R
        
