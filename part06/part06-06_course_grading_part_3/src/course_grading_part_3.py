# tee ratkaisu tänne
# wwite your solution here
# write your solution here
def student_exercises(s_file:str, e_file:str, exam_file:str)->None:
    
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
            
    exams={}
    
    with open(exam_file) as exam_list:
        
        for line in exam_list:
            line=line.strip()
            parts=line.split(";")
            if parts[0]=="id":
                continue
            exams[parts[0]]=list(map(int,parts[1:]))
    
    p_name="name"
    p_exec_nbr="exec_nbr"
    p_exec_pts="exec_pts."
    p_exm_pts="exm_pts."
    p_tot_pts="tot_pts."
    p_grade="grade"    
    print(f"{p_name:30}{p_exec_nbr:10}{p_exec_pts:10}{p_exm_pts:10}{p_tot_pts:10}{p_grade:10}\n")        
    
    for s_id in students:
        if s_id in exercises:
            name=students[s_id]
            tot_ex_points=sum(exercises[s_id])
            ex_points=tot_ex_points//4
            exam_points=sum(exams[s_id])
            total_points=ex_points+exam_points
            
            grade=0
            if total_points<=14:
                grade=0
            elif total_points>=15 and total_points<=17:
                grade=1
            elif total_points>=18 and total_points<=20:
                grade=2
            elif total_points>=21 and total_points<=23:
                grade=3
            elif total_points>=24 and total_points<=27:
                grade=4
            elif total_points>=28:
                grade=5
            
            print(f"{name:30}{tot_ex_points:<10}{ex_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}")
            
            
            
            
    
    
def main():
    
    
    if True:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_points=input("Exam points: ")
        student_exercises(student_info, exercise_data, exam_points)
    else:
        # hard-coded input
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_points="exam_points1.csv"
        student_exercises(student_info, exercise_data, exam_points)


main()