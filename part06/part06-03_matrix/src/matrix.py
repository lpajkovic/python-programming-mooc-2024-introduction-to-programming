# write your solution here
def row_sums()->list:

    r_sums=[]
    with open("matrix.txt") as matrix_file:
  
        for line in matrix_file:
            line=line.replace("\n", "")
            values=list(map(int,line.split(",")))
            r_sums.append(sum(values))
        
    return r_sums
            
def row_maxes()->list:
    
    r_max=[]
    
    with open("matrix.txt") as matrix_file:
        
        for line in matrix_file:
            line=line.replace("\n", "")
            values=list(map(int,line.split(",")))
            r_max.append(max(values))
            
    return r_max

def matrix_sum()->int:
    
    return sum(row_sums())

def matrix_max()->int:
    
    return max(row_maxes())

if __name__=="__main__":
    matrix_sum()
    matrix_max()
    