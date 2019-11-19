from numpy import convolve
import itertools
from numpy.polynomial import polynomial as polynom
import numpy as np

class ExtensionField:
    """
    A class used to represent a Galois Field with 
    corresponding attributes and methods described below.
    ...
    Attributes
    ----------
    field_polynom : list
        an array of integers that represents the field polynomial
    degree : int
        integer to represent degree of polynomial field
    prime : int
        the integer to represent the prime field
    number_of_elements : int
        integer that is calculated on a fly and represents number of elements in a field 
    Methods
    -------
    generate_elements()
        used as a helper methods in constructor; generates elements in a field
    
    add_using_polynom(c1,c2)
        takes two int[] arguments
        used as a helper methods for adding two polynomials

    multiply_using_polynom(c1,c2)
        takes two int[] arguments
        used as a helper methods for multiplying two polynomials
    
    
    """


    def __init__(self,degree,prime,field_polynom):
        self.field_polynom=field_polynom
        self.degree=degree
        self.prime=prime
        self.number_of_elements=prime**degree
        self.__generate_elements()

    def __generate_elements(self):
        """Helper to map elements to polynoms"""
        
        prime_elements=[]
        for i in range(0,self.prime):
            prime_elements.append(i)
        self.elements={}
        count = 0
        elements_at_positions=itertools.product(prime_elements,repeat=self.degree)
        for i in elements_at_positions:
            self.elements.update({count:i})
            count+=1
        
        return self.elements
    
    
    def add_using_polynom(self,c1,c2):
        """Adds using two polynoms from GaloisField """
        sum_of_polynoms = np.polyadd(c1,c2)
        sum_of_polynoms_upgraded = []
        for element in sum_of_polynoms:
            sum_of_polynoms_upgraded.append((int(element))%self.prime)
        return tuple(sum_of_polynoms_upgraded)
    
    def __check_negativity(self, c1,c2):
                #check element c1
        n1=0
        n2=0
        if (c1>0):
            n1 = c1%self.number_of_elements
        elif (c1<0):
            n1 = self.additive_inverse(c1)
        #check element c2
        if (c2>0):
            n2 = c2%self.number_of_elements
        elif (c2<0):
            n2 = self.additive_inverse(c2)
        return n1,n2
    
    def add(self,c1,c2):
        """Adds using two numbers from GaloisField """
        n1, n2 = self.__check_negativity(c1,c2)
        
        a1=self.elements[n1]
        a2=self.elements[n2]
        sum_of_polynoms_upgraded = self.add_using_polynom(a1,a2)
        return self.get_element_by_polynom(tuple(sum_of_polynoms_upgraded))

    def multiply_using_polynom(self,c1,c2):
        """Multiplies using two polynoms from GaloisField """
        
        multiple_of_polynoms = np.polymul(c1,c2)
        polynom_in_GaloisField = np.polydiv(multiple_of_polynoms,self.field_polynom)
        multiple_of_polynoms_upgraded  = []
        for element in polynom_in_GaloisField[1]:
            multiple_of_polynoms_upgraded.append((int(element))%self.prime)
        
        diff = len(self.elements.get(0)) - len(multiple_of_polynoms_upgraded)
        if diff != 0:
            for i in range(0,len(self.elements.get(0))):
                if i == len(multiple_of_polynoms_upgraded):
                    multiple_of_polynoms_upgraded.insert(0,0)
        
        return tuple(multiple_of_polynoms_upgraded)

    def power(self,c1, o):
        """Returns power of c1 to p (divide-and-conquer) with linear complexity O(x)"""
        x, p = self.__check_negativity(c1,o)

        if p == 0:
            return 1
        y = 1
        while p > 1:
            if p %2 ==0:
                x = self.multiply(x, x)
                p = p / 2
            else:
                y = self.multiply(x, y)
                x = self.multiply(x, x)
                p = (p-1)/2
        
        return self.multiply(x , y)
        

    def multiply(self,c1,c2):
        """Multiplies using two numbers from GaloisField """
        n1, n2 = self.__check_negativity(c1,c2)
        a1=list(self.elements[n1])
        a2=list(self.elements[n2])
        multiple_of_polynoms = self.multiply_using_polynom(a1,a2)
        return self.get_element_by_polynom(tuple(multiple_of_polynoms))
    
    def get_polynom_by_element(self,element):
        """Return polynom at position of element"""
        p=0
        if element<0:
            p=abs(element)
        p = element % self.number_of_elements
         
        return self.elements[p]
    


    def get_element_by_polynom(self, polynom):
        """Return element at position of polynom"""
        elem = 0
        for element, polynomial in self.elements.items():    
            if polynom == polynomial:
                elem = element

        return elem % self.number_of_elements

    def order(self):
        """Find the order of any given element"""
        counter = self.number_of_elements - 1
        return counter

    def multiplicative_inverse(self, element):
        """Find the multiplicative inverse of a given element"""
        if element==0:
            return 0
        elif element==1:
            return 1
        power_of_inverse = self.order() - 1
        a_minus_one = self.power(element,power_of_inverse)
        return a_minus_one
    

    
    def subtract(self,c1,c2):
        """Subtract c2 from c1"""
        return self.add(c1,self.additive_inverse(c2))

    def divide(self,c1,c2):
        """Divide c1 by c2"""
        return self.multiply(c1,self.multiplicative_inverse(c2))
   
    def additive_invs(self, element):
        """Additive inverse calculator"""
        polynom_for_add_inv = []
        for i in range(self.degree):
            if i == self.degree-1:
                polynom_for_add_inv.append(self.order())
            else:
                polynom_for_add_inv.append(0)
        
        element_polynom=list(self.get_polynom_by_element(element))
        return self.get_element_by_polynom(self.multiply_using_polynom(element_polynom,polynom_for_add_inv))
    
    def additive_inverse(self, element):
        """Additive inverse calculator"""
        inverse = 0
        element_this = abs(element)
        for element_other in self.elements:
            if self.add(element_this,element_other) == 0:
                inverse=element_other
                break
        return inverse
