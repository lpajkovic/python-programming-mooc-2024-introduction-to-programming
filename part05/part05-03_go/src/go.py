# Write your solution here
def who_won(game_board:list)->int:
    p1_pieces=0
    p2_pieces=0
    for row in game_board:
        for value in row:
            if value==1:
                p1_pieces+=1
            elif value==2:
                p2_pieces+=1
    if p1_pieces>p2_pieces:
        return 1
    elif p1_pieces<p2_pieces:
        return 2
    return 0
    
if __name__=="__main__":
    go=who_won([[1,2,3],[1,0,2], [2,1,1]])