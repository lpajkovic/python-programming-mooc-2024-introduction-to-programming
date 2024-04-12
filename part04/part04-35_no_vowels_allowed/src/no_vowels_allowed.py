# Write your solution here
def no_vowels(word:str)->str:
    word=word.replace("a","")
    word=word.replace("e","")
    word=word.replace("i","")
    word=word.replace("o","")
    word=word.replace("u","")
    return word


if __name__=="__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))