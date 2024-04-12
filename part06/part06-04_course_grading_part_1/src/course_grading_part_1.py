# write your solution here
def student_exercises(s_file:str, e_file:str)->None:
    
    students={}
    
    with open(s_file) as students_file:
        
        for line in students_file:
            line=line.strip()
            parts=line.split(";")
            if parts[0]=="id":
                continue
            students[parts[0]]=parts[1] + " " + parts[2]
    
    exercises={}
    
    with open(e_file) as exercises_file:
        
        for line in exercises_file:
            line=line.strip()
            parts=line.split(";")
            if parts[0]=="id":
                continue
            exercises[parts[0]]=list(map(int,parts[1:]))
    
    for s_id in students:
        if s_id in exercises:
            name=students[s_id]
            ex_points=sum(exercises[s_id])
            print(f"{name} {ex_points}")
    
    
def main():
    
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    student_exercises(student_info, exercise_data)
    


main()