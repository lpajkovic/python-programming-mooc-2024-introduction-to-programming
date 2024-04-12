# Write your solution here
def same_chars(word, c1, c2):
    if c1>=len(word) or c2>=len(word):
        return False
    return word[c1]==word[c2]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))