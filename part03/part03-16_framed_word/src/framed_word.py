# Write your solution here
word=input("Word: ")

left=(28-len(word))//2

if len(word)%2!=0:
    right=left+1
else:
    right=left


printSpaceL=" "*int(left)
printSpaceR=" "*int(right)
print("*"*30)
print(f"*{printSpaceL}{word}{printSpaceR}*")
print("*"*30)