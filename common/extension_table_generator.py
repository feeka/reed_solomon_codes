from common.extension_field import ExtensionField

class ExtensionFieldTableGenerator:
    
    def __init__(self,degree,prime,polynom):
        self.polynom_field=ExtensionField(degree,prime,polynom)
        if(self.__generate_additive_inverses()):
            print("successfully built additive_inverses")
        if(self.__generate_multiplicative_inverses()):
            print("successfully built multiplicative inverses")
       
        if(self.__generate_addition_lookup()):
            print("successfully built addition_table")
        if(self.__generate_multiplication_lookup()):
            print("successfully built multiplication_table")
        if(self.__generate_subtract_lookup()):
            print("successfully built subtract_table")
        if(self.__generate_divide_lookup()):
            print("successfully built divide_table")
        
        if(self.__generate_power_lookup()):
            print("successfully built power_table")
        

    
    def __generate_additive_inverses(self):
        self.add_inverse = {}
        success = False
        for k,i in self.polynom_field.elements.items():
            success = False
            self.add_inverse.update({k:self.polynom_field.additive_inverse(k)})
            
            success = True
        return success

    def __generate_multiplicative_inverses(self):
        self.mult_inverses = {}
        success = False
        for k,i in self.polynom_field.elements.items():
            success = False
            self.mult_inverses.update({k:self.polynom_field.multiplicative_inverse(k)})
            print(self.polynom_field.multiplicative_inverse(k))
            success = True
        return success
    
    def __generate_multiplication_lookup(self):
        """Multiplicative table"""
        self.mul_table = {}
        success = False
        for i in self.polynom_field.elements:
            for j in self.polynom_field.elements:
                success = False
                self.mul_table.update({str(i)+"*"+str(j):self.polynom_field.multiply(i,j)})
                success = True
        return success
    
    def __generate_addition_lookup(self):
        """Multiplicative table"""
        self.add_table = {}
        success = False
        for i in self.polynom_field.elements:
            for j in self.polynom_field.elements:
                success = False
                self.add_table.update({str(i)+"+"+str(j):self.polynom_field.add(i,j)})
                success = True
        return success

    def __generate_power_lookup(self):
        self.power_table = {}
        success = False
        powers = []
        for i in range(0,self.polynom_field.number_of_elements):
            powers.append(i)
        for i in self.polynom_field.elements:
            for p in powers:
                success = False
                self.power_table.update({str(i)+"^"+str(p):self.polynom_field.power(i,p)})
                success = True
                
        return success


    def __generate_divide_lookup(self):
        """Multiplicative table"""
        self.div_table = {}
        success = False
        for i in self.polynom_field.elements:
            for j in self.polynom_field.elements:
                success = False
                self.div_table.update({str(i)+"/"+str(j):self.polynom_field.divide(i,j)})
                success = True
        return success
    
    def __generate_subtract_lookup(self):
        """Multiplicative table"""
        self.subt_table = {}
        success = False
        for i in self.polynom_field.elements:
            for j in self.polynom_field.elements:
                success = False
                self.subt_table.update({str(i)+"-"+str(j):self.polynom_field.subtract(i,j)})
                success = True
        return success