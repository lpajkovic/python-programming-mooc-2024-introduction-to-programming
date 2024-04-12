# Write your solution here
while True:
    number=int(input("Please type in a number: "))
    if number<=0:
        print("Thanks and bye!")
        break
    fact=1
    to_sum=number
    while to_sum>0:
        fact*=to_sum
        to_sum-=1
    print(f"The factorial of the number {number} is {fact}")