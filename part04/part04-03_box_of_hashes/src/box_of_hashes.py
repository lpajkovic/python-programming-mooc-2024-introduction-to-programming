# Copy here code of line function from previous exercise
def line(times, word):
    if word=="":
        word="*"
    print(word[0]*times)
def box_of_hashes(height):
    # You should call function line here with proper parameters
    i=0
    while i<height:
        i+=1
        line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
