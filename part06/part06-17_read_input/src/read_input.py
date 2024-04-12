# Write your solution here

def read_input(message:str, lower: int, upper: int)->int:
    
    while True:
        try:
            typed_num=int(input(message))
            if typed_num>=lower and typed_num<=upper:
                return typed_num
        except ValueError:
            pass
        
        print(f"You must type in an integer between {lower} and {upper}")
        


if __name__=="__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)