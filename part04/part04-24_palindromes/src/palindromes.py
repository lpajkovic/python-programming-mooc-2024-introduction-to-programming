# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word:str) -> bool:
    #if len(word)%2!=0:
    #    return False
    #i=0
    #j=len(word)-1
    #while i<=j:
    #    if word[i]!=word[j]:
    #        return False
    #    i+=1
    #    j-=1
    #return True
    
    reversed_word=''.join(reversed(word))
    if word==reversed_word:
        return True
    return False

def main():
    while True:
        word=input("Please type in a palindrome: ")
        pal=palindromes(word)
        if pal:
            print(f"{word} is a palindrome!")
            break
        print("that wasn't a palindrome")


main()
    