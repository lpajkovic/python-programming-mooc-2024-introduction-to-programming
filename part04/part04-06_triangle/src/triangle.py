# Copy here code of line function from previous exercise
def line(times, word):
    if word=="":
        word="*"
    print(word[0]*times)
    
def triangle(size):
    # You should call function line here with proper parameters
    i=1
    while i<=size:
        line(i, "#")
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)