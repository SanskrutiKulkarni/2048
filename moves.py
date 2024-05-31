
#left, right, down, up



def lg(num): # mapping box_color to the value in the cell of grid
    if(num==0): return 0
    if(num==2): return 1
    if(num==4): return 2
    if(num==8): return 3
    if(num==16): return 4
    if(num==32): return 5
    if(num==64): return 6
    if(num==128): return 7
    if(num==256): return 8
    if(num==512): return 9
    if(num==1024): return 10
    if(num==2048): return 11
    return 12




def transpose(mat):
    new_mat = [] # empty list to sore the new matrix
    for i in range(4):
        new_mat.append([]) # internal list
        for j in range(4):
            new_mat[i].append(mat[j][i]) # transposed index elements
    return new_mat

# helps to tarnsition between row based and column base operations

def move_up(board):  # move left

    ok = False # whether any tile has moved
    just = True # used to handle merging the tiles

    ret = {}
 # iterates over each row of the game grid
    for i in range(4):
        X = [] # to store the new row after the movement
        j = 0 # iterates over the column
        while(j<4):
            if(just == False):
                if(len(X)>0 and X[len(X)-1]==board[i][j]):
                    just = True
                    el = X.pop()*2 # just last element
                    X.append(el) # 2 2 same row combined
                else:
                    if(board[i][j]!=0):  # not empty , current state in that row
                        X.append(board[i][j]) # put it in X
            elif(board[i][j]!=0):
                X.append(board[i][j])
                just = False
            j+=1          
            
        while(len(X)<4):
            X.append(0)
        ret[i] = X
    
    for i in range(4):
        for j in range(4):
            if(board[i][j]!=ret[i][j]): ok=True # changes are made

    return ret,ok # new grid and the change

    

def move_down(board): # move right

    ok = False
    just = True

    ret = {}

    for i in range(4):
        X = []
        j = 3
        
        while(j>=0):
            if(just == False):
                if(len(X)>0 and X[len(X)-1]==board[i][j]):
                    just = True
                    el = X.pop()*2
                    X.append(el)
                else:
                    if(board[i][j]!=0):
                        X.append(board[i][j])
            elif(board[i][j]!=0):
                X.append(board[i][j])
                just = False
            j-=1       
        

        #X.reverse()
        while(len(X)<4):
            X.append(0)
        X.reverse()
        ret[i] = X
    
    for i in range(4):
        for j in range(4):
            if(board[i][j]!=ret[i][j]): ok=True

    return ret,ok



def move_left(board): # move up
    
    ok = False
    ret = transpose(board)
    ret,ok = move_up(ret)
    ret = transpose(ret)
    return ret,ok


def move_right(board): # move down

    ok = False
    ret = transpose(board)
    ret,ok = move_down(ret)
    ret = transpose(ret)
    return ret,ok
    
    
