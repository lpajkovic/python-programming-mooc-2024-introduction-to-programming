def add_student(students:dict, name:str)->None:
    
    students[name]=[]
    
def print_student(students:dict, name:str)->None:
    
    if name in students:
        print(name + ":")
        if len(students[name])==0:
            print(" no completed courses")
        else:
            avg=0
            courses=len(students[name])
            print(f" {courses} completed courses:")
            for course in students[name]:
                print(f"  {course[0]} {course[1]}")
                avg+=course[1]
            avg/=courses
            print(f" average grade {avg:.1f}")
            #print(f" {students[name]}")
    else:
        print(f"{name}: no such person in the database")
        
def add_course(students:dict, name:str, course:tuple)->None:
    
    if name in students:
        students[name].append(course)
        
if __name__=="__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")