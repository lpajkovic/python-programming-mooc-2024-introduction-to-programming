# Write your solution here
values=[]
i=1
print(f"The list is now {values}")
while True:
    
    command=input("a(d)d, (r)emove or e(x)it: ")
    if command=="d":
        values.append(i)
        print(f"The list is now {values}")
        i+=1
    elif command=="r":
        values.pop(-1)
        print(f"The list is now {values}")
        i-=1
    elif command=="x":
        print("Bye!")
        break
    
