# Write your solution here
year=int(input("Year: "))
yearLeap=year
while True:
    yearLeap+=1
    if yearLeap%4==0:
        if yearLeap%100==0:
            if yearLeap%400==0:
                print(f"The next leap year after {year} is {yearLeap}")
                break
        else:
            print(f"The next leap year after {year} is {yearLeap}")
            break
        