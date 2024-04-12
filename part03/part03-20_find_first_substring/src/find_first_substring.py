# Write your solution here
word=input("Please type in a word: ")
char=input("Please type in a character: ")

index=word.find(char)
if index!=-1:
    if len(word)-index>=3:
        print(word[index:(index+3)])