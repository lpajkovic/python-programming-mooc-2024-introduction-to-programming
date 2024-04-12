# Write your solution here
def squared(word, times):
    word_squared=word*times
    i=0
    temp_len=0
    while i<times:
        j=0
        while j<times:
            j+=1
            print(word_squared[temp_len],end="")
            temp_len+=1
            if temp_len==len(word_squared):
                temp_len=0
        print("")
        i+=1
        

if __name__=="__main__":
    squared("ab", 3)