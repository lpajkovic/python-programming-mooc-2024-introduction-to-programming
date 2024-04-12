# Write your solution here
passwd=input("Password: ")
while True:
    rpt=input("Repeat password: ")
    if rpt==passwd:
        print("User account created!")
        break

    print("They do not match!")