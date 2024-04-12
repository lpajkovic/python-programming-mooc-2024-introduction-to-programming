# Write your solution here
def row_correct(sudoku:list,row_no:int)->bool:
    
    visited_nums=[]
    for i in range(0,9):
        if sudoku[row_no][i]>0 and sudoku[row_no][i] in visited_nums:
            return False
        else:
            visited_nums.append(sudoku[row_no][i])
    return True

def column_correct(sudoku:list, column_no:int)->bool:
    visited_nums=[]
    for i in range(0,9):
        if sudoku[i][column_no]>0 and sudoku[i][column_no] in visited_nums:
            return False
        else:
            visited_nums.append(sudoku[i][column_no])
    return True
    
def block_correct(sudoku:list,row_no:int,column_no:int)->bool:
    visited_nums=[]
    for i in range(row_no,row_no+3):
        for j in range(column_no,column_no+3):
            
            if sudoku[i][j]>0 and sudoku[i][j] in visited_nums:
                return False
            else:
                visited_nums.append(sudoku[i][j])
    return True

def sudoku_grid_correct(sudoku:list)->bool:
    correct=True
    for row in range(0,len(sudoku)):
        correct= correct and row_correct(sudoku,row)
    for column in range(0,len(sudoku)):
        correct= correct and column_correct(sudoku,column)
    for row in range(0,len(sudoku),3):
        for column in range(0,len(sudoku),3):
            correct= correct and block_correct(sudoku, row, column)
    return correct

if __name__=="__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))