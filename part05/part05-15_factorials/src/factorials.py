# Write your solution here
def factorials(n:int)->dict:
    ret_dict={}
    value=1
    for i in range(1,n+1,1):
        value*=i
        ret_dict[i]=value
    
    return ret_dict
    


if __name__=="__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])