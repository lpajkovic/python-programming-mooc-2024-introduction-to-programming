# Write your solution here
def line(times, word):
    if word=="":
        word="*"
    print(word[0]*times)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")