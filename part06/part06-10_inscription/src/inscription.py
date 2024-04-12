# Write your solution here

def main():
    name=input("Who should i sign this to: ")
    file_out=input("Where shall I save it?")
    output=f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team\n"
    with open(file_out, "w") as new_file:
        
        new_file.write(output)


main()