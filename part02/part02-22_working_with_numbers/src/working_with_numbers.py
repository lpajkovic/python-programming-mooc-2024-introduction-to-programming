# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count=0
summ=0
mean=0
pos=0
neg=0
while True:
    number=int(input("Number: "))
    if number==0:
        print(f"Numbers typed in {count}")
        print(f"The sum of the numbers is {summ}")
        print(f"The mean of the numbers is {mean}")
        print(f"Positive numbers {pos}")
        print(f"Negative numbers {neg}")
        break
    count+=1
    summ+=number
    mean=summ/count
    if number>0:
        pos+=1
    if number<0:
        neg+=1