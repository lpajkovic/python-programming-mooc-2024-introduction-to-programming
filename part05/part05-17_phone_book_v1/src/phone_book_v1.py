# Write your solution here


def main():
    pbook={}
    while True:
        command=int(input("command (1 search, 2 add, 3 quit) "))
        if command==3:
            print("quitting...")
            break
        if command==2:
            name=input("name: ")
            number=input("number: ")
            if number=="":
                print("no number")
            else:
                pbook[name]=number
                print("ok!")
        if command==1:
            name=input("name: ")
            if name in pbook:
                print(pbook[name])
            else:
                print("no number")
            

main()