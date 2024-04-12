# Write your solution here

def histogram(word:str)->None:
    letters={}
    for i in range(0,len(word)):
        letter=word[i]
        if letter not in letters:
            letters[letter]=[]
        letters[letter].append(letter)
    
    for key, values in letters.items():
        print(f'{key} {len(values)*"*"}')


if __name__=="__main__":
    histogram("abba")