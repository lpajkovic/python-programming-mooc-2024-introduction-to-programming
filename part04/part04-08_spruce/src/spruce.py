# Write your solution here
def line(times, word):
    if word=="":
        word="*"
    return (word[0]*times)
    
def spruce(length):
    print("a spruce!")
    i=1
    while i<=length:
    
        num_stars=2*i-1
        num_blank=((2*length-1)-num_stars)//2
        stars=line(num_stars,"*")
        print(f'{num_blank*" "}{stars}{num_blank*" "}')
        i+=1
    num_stars=1
    num_blank=((2*length-1)-num_stars)//2
    stars=line(num_stars,"*")
    print(f'{num_blank*" "}{stars}{num_blank*" "}')
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)