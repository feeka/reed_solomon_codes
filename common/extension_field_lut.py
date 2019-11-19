from common.extension_table_generator import ExtensionFieldTableGenerator


def extension_field(degree,prime,field_polynom):
    table_gen = ExtensionFieldTableGenerator(degree,prime,field_polynom)
    num_of_elems=prime**degree
    class LookupTablesForGaloisField:

        def __init__(self,el):
            self.n = 0
            if el<0:
                self.n = table_gen.polynom_field.additive_inverse(el)
            elif el>0:
                self.n = el % num_of_elems

            self.field = LookupTablesForGaloisField
        #done
        def __add__(self,other):
            c1=self.n
            c2=other.n
            addition_table = table_gen.add_table
            element_one=str(c1)
            element_two=str(c2)
            concat=element_one+"+"+element_two
            return LookupTablesForGaloisField(addition_table.get(concat))
        #done
        def __mul__(self,other):
            c1=self.n
            c2=other.n
            mul_table = table_gen.mul_table
            element_one=str(c1)
            element_two=str(c2)
            concat=element_one+"*"+element_two
            return LookupTablesForGaloisField(mul_table.get(concat))
        
        #done
        def __sub__(self, other):
            c1=self.n
            c2=other.n
            sub_table = table_gen.subt_table
            element_one=str(c1)
            element_two=str(c2)
            concat=element_one+"-"+element_two
            return LookupTablesForGaloisField(sub_table.get(concat))        
        
        def __truediv__(self,other):
            c1=self.n
            c2=other.n
            return self.__div_helper(c1,c2)
        #done
        def __div__(self, other):
            c1=self.n
            c2=other.n
            return self.__div_helper(c1,c2)
        
        def __div_helper(self,c1,c2):
            div_table = table_gen.div_table
            element_one=str(c1)
            element_two=str(c2)
            concat=element_one+"/"+element_two
            return LookupTablesForGaloisField(div_table.get(concat))
        
        #done
        def __str__(self): return str(self.n)
        #done
        def __pow__(self,other):
            c1=self.n
            c2=other.n
            pow_table = table_gen.power_table
            element_one=str(c1)
            element_two=str(c2)
            concat=element_one+"^"+element_two
            return LookupTablesForGaloisField(pow_table.get(concat))
        
        def __eq__(self, other): 
            return isinstance(other, LookupTablesForGaloisField) and self.n == other.n

        def __abs__(self): return abs(self.n)

        def multiplicative_inverse(self):
            el=self.n
            mul_invs=table_gen.mult_inverses
            return mul_invs.get(el)
        
        def __divmod__(self, divisor):
            return self.__div_helper(self.n,divisor.n)

        def __repr__(self): 
            t=0
            return '%d (mod %d)' % (self.n, num_of_elems)
            
            
        
        def __neg__(self):
            add_invs=table_gen.add_inverse
            return LookupTablesForGaloisField(add_invs.get(abs(self.n)))
            
    
    LookupTablesForGaloisField.prime = prime
    LookupTablesForGaloisField.field_polynom = field_polynom
    LookupTablesForGaloisField.degree = degree

    LookupTablesForGaloisField.__name__ = 'Z/%d' % (num_of_elems)
    return LookupTablesForGaloisField
