# Write your solution here

from datetime import datetime

def main():
    
    day=int(input("Day: "))
    month=int(input("Month: "))
    year=int(input("Year: "))
    
    dob=datetime(year, month, day)
    new_mil=datetime(1999,12,31)
    diff=new_mil-dob
    
    if diff.days<=0:
        print("You weren't born yet on the eve of the new millennium.")
    else:
        print(f"You were {diff.days} days old on the eve of the new millennium.")



main()