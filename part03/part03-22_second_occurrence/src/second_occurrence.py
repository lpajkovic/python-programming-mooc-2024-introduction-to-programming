# Write your solution here
word=input("Please type in a string: ")
substring=input("Please type in a substring: ")

first_occ=word.find(substring)
second_occ=-1

if first_occ!=-1:
    second_occ=word.find(substring,first_occ+len(substring))

if second_occ!=-1:
    print(f"The second occurrence of the substring is at index {second_occ}.")
else:
    print("The substring does not occur twice in the string.")
    