# Write your solution here
i=int(input("How many items: "))
j=1
items=[]
while j<=i:
    #print(f"Item {j}: ", end="")
    item=int(input(f"Item {j}: "))
    items.append(item)
    j+=1
print(items)