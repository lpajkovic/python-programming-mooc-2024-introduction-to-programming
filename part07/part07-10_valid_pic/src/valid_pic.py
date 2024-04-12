# Write your solution here
from datetime import datetime


def is_it_valid(pic:str)->bool:
    
    if len(pic)!=11:
        return False
    
    day=int(pic[0:2])
    month=int(pic[2:4])
    year=int(pic[4:6])
    marker=pic[6]
    pers_id=pic[7:10]
    pic_control=pic[10]
    control_num=pic[0:6]+pers_id
    control_pos=int(control_num)%31
    control_c="0123456789ABCDEFHJKLMNPRSTUVWXY"[control_pos]
    
    if day<1 or day>31 or month<1 or month>12 or marker not in ("-", "+", "A") or pic_control!=control_c:
        return False
    
    
    fullyear=0
    if marker=="-":
        fullyear=1800
    elif marker=="+":
        fullyear=1900
    elif marker=="A":
        fullyear=2000
        
    fullyear+=year
    
    try:
        x=datetime(fullyear, month, day)
        print(x)
        return True
    except:
        return False
    
if __name__=="__main__":
    valid=is_it_valid("290200-1239")
    print(valid)
    
