# Write your solution here
limit=int(input("Limit: "))
i=1
j=2
output=f"The consecutive sum: {i}"
while i<limit:
    i+=j
    output+=f" + {j}"
    j+=1
output+=f" = {i}"
print(output)