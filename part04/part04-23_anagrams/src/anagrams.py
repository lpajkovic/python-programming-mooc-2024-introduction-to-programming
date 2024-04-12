# Write your solution here
def anagrams(string1:str, string2:str) -> bool:
    string1=sorted(string1)
    string2=sorted(string2)
    if string1==string2:
        return True
    return False

if __name__=="__main__":
    print(anagrams("tame", "meta"))