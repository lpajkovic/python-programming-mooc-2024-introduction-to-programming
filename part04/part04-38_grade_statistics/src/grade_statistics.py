# Write your solution here
def exercise_points(grades:list)->int:
    return grades[1]//10

def total_points(grades:list, exam_pts:int)->int:
    return grades[0]+exam_pts

def grading(tot_pts:int)->int:
    if tot_pts<=14:
        return 0
    elif tot_pts>=15 and tot_pts<=17:
        return 1
    elif tot_pts>=18 and tot_pts<=20:
        return 2
    elif tot_pts>=21 and tot_pts<=23:
        return 3
    elif tot_pts>=24 and tot_pts<=27:
        return 4
    elif tot_pts>=28 and tot_pts<=30:
        return 5
    
    return -1

def grade_statistic(grades:list)->list:
    exc_points=exercise_points(grades)
    tot_points=total_points(grades,exc_points)
    grade=grading(tot_points)
    if grades[0]<10:
        grade=0
    
    return [grade,tot_points]

def point_avg(points:list)->float:
    return sum(points)/len(points)

def pass_avg(grades:list, points:list)->float:
    num_passed=0
    
    for grade in grades:
        if grade>=1:
            num_passed+=1
    
    return (num_passed/len(points))*100

def user_input()->None:
    points=[]
    grades=[]
    while True:
        points_in=list(input("Exam points and exercises completed: ").split())
        points_in=[int(i) for i in points_in]
        if len(points_in)==0:
            break
        grade_points=grade_statistic(points_in)
        points.append(grade_points[1])
        grades.append(grade_points[0])
    
    print("Statistics: ")
    avg_points=point_avg(points)
    avg_pass=pass_avg(grades, points)
    print(f"Points average: {avg_points:.1f}")
    print(f"Pass percentage: {avg_pass:.1f}")
    print("Grade distribution: ")
    for grade in range(5, -1, -1):
        print(f'{" "*2}{grade}: ',end='')
        for i in grades:
            if i==grade:
                print("*",end="")
        print("")
    
    
def main():
    user_input()
    
main()