# write your solution here
def read_fruits()->dict:
    
    ret_fruits={}
    
    with open("fruits.csv") as fruits_file:
        
        for line in fruits_file:
            line=line.replace("\n", "")
            values=line.split(";")
            ret_fruits[values[0]]=float(values[1])
    
    return ret_fruits


if __name__=="__main__":
    read_fruits()