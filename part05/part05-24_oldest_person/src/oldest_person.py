# Write your solution here
def oldest_person(persons:list)->str:
    max_age=3000
    max_name=""
    for person in persons:
        print(person)
        
        if person[1]<max_age:
            max_age=person[1]
            max_name=person[0]
    
    return max_name

if __name__=="__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))