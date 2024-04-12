# Write your solution here
let1=input("1st letter: ")
let2=input("2nd letter: ")
let3=input("3rd letter: ")
middle=""
if let1>let2 and let1<let3:
    middle=let1
elif let2>let3 and let2<let1:
    middle=let2
elif let3>let2 and let3<let1:
    middle=let3
elif let1<let2 and let1>let3:
    middle=let1
elif let2<let3 and let2>let1:
    middle=let2
elif let3<let2 and let3>let1:
    middle=let3

print(f"The letter in the middle is {middle}")