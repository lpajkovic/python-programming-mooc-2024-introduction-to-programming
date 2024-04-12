# Write your solution here
def all_the_longest(my_list:list)->list:
    
    longest=len(my_list[0])
    for item in my_list:
        if len(item)>longest:
            longest=len(item)
    ret_list=[]
    for item in my_list:
        if len(item)==longest:
            ret_list.append(item)
    return ret_list
            

if __name__=="__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']