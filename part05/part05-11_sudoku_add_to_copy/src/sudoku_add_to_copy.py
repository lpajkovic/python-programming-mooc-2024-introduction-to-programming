# Write your solution here
def print_sudoku(sudoku:list)->None:
    printed_sudoku=sudoku[:]
    
    for i in range(0,9):
        for j in range(0,9):
            if printed_sudoku[i][j]==0:
                print("_",end=" ")
            else:
                print(printed_sudoku[i][j], end=" ")
            if (j+1)%3==0:
                print(" ",end="")
        if(i+1)%3==0:
            print()
        print()
        
def copy_and_add(sudoku:list, row_no:int, column_no:int, number:int)->list:
    new_list=[]
    
    for row in sudoku:
        temp_row=[]
        for item in row:
            temp_row.append(item)
        new_list.append(temp_row)    
    new_list[row_no][column_no]=number
    return new_list


if __name__=="__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)