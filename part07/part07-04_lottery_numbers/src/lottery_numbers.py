# Write your solution here

from random import sample

def lottery_numbers(amount: int, lower: int, upper: int)->list:
    
    
    
    number_pool=list(range(lower,upper))
    draw=sample(number_pool, amount)

    return sorted(draw)

if __name__=="__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)