# Write your solution here

from fractions import Fraction

def fractionate(amount:int)->list:
    
    fracs=[]
    
    for i in range(amount):
        fracs.append(Fraction(1,amount))
        
    return fracs


if __name__=="__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))