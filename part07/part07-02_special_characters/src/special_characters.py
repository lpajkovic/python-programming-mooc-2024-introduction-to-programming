from string import ascii_letters, punctuation

def separate_characters(my_string:str)->tuple:
    
    ascii_l=""
    punct=""
    other=""
    
    for letter in my_string:
        if letter in ascii_letters:
            ascii_l+=letter
        elif letter in punctuation:
            punct+=letter
        else:
            other+=letter
            
    return (ascii_l, punct, other)