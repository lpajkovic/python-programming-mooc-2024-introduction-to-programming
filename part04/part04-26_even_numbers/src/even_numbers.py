# Write your solution here
def even_numbers(numbers:list)->list:
    nums=[]
    for num in numbers:
        if num%2==0:
            nums.append(num)
    return nums

if __name__=="__main__":
    my_list = [1, -2, 3, -4, 5]
    result = even_numbers(my_list)
    print("The result is", result)