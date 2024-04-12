# Write your solution here
def longest(words:list)->str:
    max_str=words[0]
    for word in words:
        if len(word)>len(max_str):
            max_str=word
    return max_str


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))