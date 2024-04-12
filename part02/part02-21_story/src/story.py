# Write your solution here
story=""
last_word=""
while True:
    word=input("Please type in a word: ")
    if word==last_word or word=="end":
        print(story)
        break
    story+=word + " "
    last_word=word
    
