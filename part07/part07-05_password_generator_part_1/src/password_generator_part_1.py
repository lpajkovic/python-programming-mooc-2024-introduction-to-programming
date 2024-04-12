# Write your solution here

import random
import string

def generate_password(length:int)->str:
    
    password=""
    for i in range(length):
        password+=random.choice(string.ascii_lowercase)
    
    return password