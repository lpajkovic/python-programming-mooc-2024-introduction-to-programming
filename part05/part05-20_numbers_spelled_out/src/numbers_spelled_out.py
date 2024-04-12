# Write your solution here

def dict_of_numbers()->dict:
    dictionary={}
    
    
    w_numb=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    w_tens=["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    w_teens=["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    dictionary[0]=w_numb[0]
        
    for i in range(1,100):
        for i in range(1,10):
            dictionary[i]=w_numb[i] 
        dictionary[10]="ten"
        for i in range(11,20):
            dictionary[i]=w_teens[i-11]
        i+=1
        tens_idx=0
        while i<100:
            
            if i%10==0:
                tens_idx+=1
                dictionary[i]=w_tens[tens_idx]
                i+=1
            else:
                
                for i in range(i,i+9):
                    dictionary[i]=f"{w_tens[tens_idx]}-{w_numb[i%10]}"
                i+=1
                
           
                
    #for key,value in dictionary.items():
    #    print(f"{key} - {value}")
    return dictionary
        
if __name__=="__main__":
    new_dict=dict_of_numbers()
    print(new_dict)