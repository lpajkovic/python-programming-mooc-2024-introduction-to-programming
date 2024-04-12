# Write your solution here
def transpose(matrix:list):
    
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            #??? matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]
            helper=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=helper
    
    
if __name__=="__main__":
    matrix=[[1,2,3], [4,5,6], [7,8,9]]
    print(matrix)
    transpose(matrix)
    print(matrix)