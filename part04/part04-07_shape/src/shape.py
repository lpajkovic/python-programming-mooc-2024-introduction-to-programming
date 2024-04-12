# Copy here code of line function from previous exercise and use it in your solution
def line(times, word):
    if word=="":
        word="*"
    print(word[0]*times)
    
def shape(tri_size, triangle, sq_size, square):
    i=0
    while i<tri_size:
        line(i+1,triangle)
        i+=1
    j=0
    while j<sq_size:
        line(tri_size, square)
        j+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")