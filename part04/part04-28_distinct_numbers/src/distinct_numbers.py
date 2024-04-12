# Write your solution here

def distinct_numbers(in_list:list)->list:
    ret_list=[]
    for item in in_list:
        if item not in ret_list:
            ret_list.append(item)
    return sorted(ret_list)

if __name__=="__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
        