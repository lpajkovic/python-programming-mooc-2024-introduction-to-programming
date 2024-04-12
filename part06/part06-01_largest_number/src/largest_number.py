# write your solution here

def largest() -> int:
    largest=-99999
    with open("numbers.txt") as new_file:
        
        
        for line in new_file:
            line=int(line)
            if line>largest:
                largest=line
    
    return largest

if __name__=="__main__":
    largest()
