# Write your solution here
def most_common_character(word:str)->str:
    
    most_common=word[0]
    for letter in word:
        if word.count(letter)>word.count(most_common):
            most_common=letter
    return most_common

if __name__=="__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))