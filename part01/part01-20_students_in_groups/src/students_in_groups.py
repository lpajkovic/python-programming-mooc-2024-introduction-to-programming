# Write your solution here
students=int(input("How many students on the course? "))
group=int(input("Desired group size? "))
groups_formed=students//group
if(groups_formed*group<students):
    groups_formed+=1
print(f"Number of groups formed: {groups_formed}")