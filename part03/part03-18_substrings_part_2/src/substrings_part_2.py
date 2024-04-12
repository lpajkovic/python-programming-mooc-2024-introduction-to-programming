# Write your solution here
word=input("Please type in a string: ")

length=len(word)
i=length-1
while i>=0:
    print(word[i:length])
    i-=1