# Write your solution here
sentence=input("Please type in a sentence: ")

words=sentence.split()
i=0
while i<len(words):
    word=words[i]
    print(word[0])
    i+=1