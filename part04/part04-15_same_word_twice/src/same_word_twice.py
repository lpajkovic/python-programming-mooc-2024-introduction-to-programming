# Write your solution here

words=[]
diff_words=0
while True:
    break_flag=0
    word=input("Word: ")
    for w in words:
        if w==word:
            print(f"You typed in {diff_words} different words")
            break_flag=1
            break
    if break_flag==1:
        break
    words.append(word)
    diff_words+=1