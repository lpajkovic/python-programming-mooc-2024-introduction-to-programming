# Write your solution here

from math import sqrt

def hypotenuse(num1:float, num2:float)->float:
    
    return sqrt(num1*num1+num2*num2)



if __name__=="__main__":
    print(hypotenuse(3,4)) # 5.0
    print(hypotenuse(5,12)) # 13.0
    print(hypotenuse(1,1)) # 1.4142135623730951