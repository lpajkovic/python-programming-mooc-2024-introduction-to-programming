# write your solution here

def main():
    sentence=input("Write text: ")
    
    words=sentence.split(" ")
    sent_words=[]
    with open("wordlist.txt") as correct_words:
        
        for line in correct_words:
            line=line.replace("\n", "")
            sent_words.append(line)
    
    for word in words:
        if word.lower() not in sent_words:
            print(f"*{word}* ", end="")
        else:
            print(f"{word} ", end="")

        
main()