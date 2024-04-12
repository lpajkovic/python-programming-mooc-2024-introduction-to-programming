# Write your solution here
wage=float(input("Hourly wage: "))
hours=int(input("Hours worked: "))
day=input("Day of the week: ")
wages=wage*hours

if day=="Sunday":
    wages*=2

print(f"Daily wages: {wages} euros")