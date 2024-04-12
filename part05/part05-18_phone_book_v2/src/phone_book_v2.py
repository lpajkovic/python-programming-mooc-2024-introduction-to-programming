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
            if name not in pbook:
                pbook[name]=[]
            if number=="":
                print("no number")
            else:
                pbook[name].append(number)
                print("ok!")
        if command==1:
            name=input("name: ")
            if name in pbook:
                #print(pbook[name])
                for value in pbook[name]:
                    print(value)
            else:
                print("no number")
            

main()