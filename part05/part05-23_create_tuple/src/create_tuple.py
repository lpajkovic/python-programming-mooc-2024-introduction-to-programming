# Write your solution here

def create_tuple(x:int, y:int, z:int)->tuple:
    first=min(x,y,z)
    second=max(x,y,z)
    third=x+y+z
    
    return (first,second,third)



if __name__ == "__main__":
    print(create_tuple(5, 3, -1))