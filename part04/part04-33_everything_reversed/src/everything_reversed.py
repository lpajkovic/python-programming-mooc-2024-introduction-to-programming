# Write your solution here
def everything_reversed(to_reverse:list)->list:
    
    ret_list=[]
    for item in to_reverse:
        ret_list.append(item[::-1])
    ret_list.reverse()
    return ret_list

if __name__=="__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)