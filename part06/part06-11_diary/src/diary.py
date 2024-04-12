# Write your solution here

def call_diary(operation:int, entry:str)->None:
    
    if operation==1:
        with open("diary.txt", "a") as diary:
            diary.write(f"{entry}\n")
        print("Diary saved")
    elif operation==2:
        with open("diary.txt") as diary:
            print("Entries:")
            for entry in diary:
                print(entry)

def main():
    
    while True:
        entry=None
        print("1 - add an entry, 2 - read entries, 0 - quit")
        command=int(input("Function: "))
        if command==0:
            print("Bye now!")
            break
        if command==1:
            entry=input("Diary entry: ")

        call_diary(command, entry)
        



main()