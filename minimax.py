from moves import*
import random

MAXDEPTH = 4 # till waht depth will the AI search

# fitness = {} # dictioanry , fitness values for different tile configuration
# for i in range(4):
#     fitness[i] = [] # initailised with empty value
# # each key corresponds to a row
# fitness[0] = [2048, 1024, 64, 32]
# fitness[1] = [512, 128, 16, 2]
# fitness[2] = [256, 8, 2, 1]
# fitness[3] = [4, 2, 1, 1]



gradient_mat = [

			[[ 64,  16,  4,  0],[ 16,  4,  0, -4],[ 4,  0, -4, -16],[ 0, -4, -16, -64]],

			[[ 0,  4,  16,  64],[-4,  0,  4,  16],[-16, -4,  0,  4],[-64, -16, -4, 0]],

			[[ 0, -4, -16, -64],[ 4,  0, -4, -16],[ 16,  4,  0, -4],[ 64,  16,  4,  0]],

			[[-64, -16, -4,  0],[-16, -4,  0,  4],[-4,  0,  4,  16],[ 0,  4,  16, 64]]
]




def TerminalState(board):

    for i in range(4):
        for j in range(4):
            if(board[i][j] == 0): return False # empty

    for i in range(4):
        for j in range(4):
            if(i+1<4 and board[i][j]==board[i+1][j]): # same value for 2 different rows but same column
                return False
            if(j+1<4 and board[i][j]==board[i][j+1]): # two diff col
                return False

    return True # jab no more moves available , end


def score(board):

    if(TerminalState(board)):
        return -1e9 # penalty

    sum = [0,0,0,0] # tarck of sum vales in each row
    # nonEmpty = 0
    mx = 0 # max tile value

    tot = 0 # toatl sum of all tile values

    for i in range(4):
        for j in range(4):
            for k in range(4):
                mx = max(mx, board[j][k])
                tot+=board[j][k]
                sum[i]+=(board[j][k]**1.25)*gradient_mat[i][j][k] # weighted sum

    ret = max(sum)+(tot/2) # rickness of tile and the distribution across the row
    if(mx!=board[0][0] and mx!=board[0][3] and mx!=board[3][0] and mx!=board[3][3]):
        ret/=2
        # to prevent clustering of tiles at the corner

    return ret


def minimax(board,depth, alpha, beta, maximizingPlayer):
# we are using alpha beta pruning
# aplha the best vale maximising player can have
# beta is best value minimising player can have
# maximizing Player -> boolean indicating whether it is a mximising or minimising player
    if(TerminalState(board) or depth==MAXDEPTH):
        return score(board)

    brk = False

    if(maximizingPlayer): # maximising AI player
        bestVal = -1e9 # initialise
        #check left child
        if(brk==False):
            new_Board,dummy = move_left(board) # left move (up )
            value = minimax(new_Board,  depth+1, alpha, beta, False) # recursively call with minimising
            bestVal = max(bestVal, value) # bestVal updated
            if(beta<=bestVal): # we always want alpha > beta
                brk = True
            alpha = max(alpha, bestVal)
            # discarded if the beta is greater than bestVal


        #check right child
        if(brk==False):
            new_Board,dummy = move_right(board)
            value = minimax(new_Board,  depth+1, alpha, beta, False) # recursive we use dfs
            bestVal = max(bestVal, value)
            if(beta<=bestVal):
                brk = True
            alpha = max(alpha, bestVal)


        #check up child
        if(brk==False):
            new_Board,dummy = move_up(board)
            value = minimax(new_Board,  depth+1, alpha, beta, False)
            bestVal = max(bestVal, value)
            # alpha = max(alpha, bestVal)
            if(beta<=bestVal):
                brk = True
            alpha = max(alpha, bestVal)


        #check down child
        if(brk==False):
            new_Board,dummy = move_down(board)
            value = minimax(new_Board,  depth+1, alpha, beta, False)
            bestVal = max(bestVal, value)
            if(beta<=bestVal):
                brk = True
            alpha = max(alpha, bestVal)

        
        # new_Board = board # this is used in the minimising
        return bestVal
    
    else:
   # we start with maximising
        Full = True
        for i in range(4):
            for j in range(4):
                if(board[i][j] == 0): Full = False

        if(Full): return minimax(board, depth+1, alpha, beta, True) # if full just go to termination condition , to maximising
        # else , bestVal max possible
        bestVal = 1e15
        brk = False
        for i in range(4):
            if(brk):break # the move is done
            for j in range(4):
                if(board[i][j]>0):continue # not empty
                new_Board = board # if empty
                new_Board[i][j] = 2 # add a 2

                value = minimax(new_Board, depth+1, alpha, beta, True)

                bestVal = min(bestVal, value)
                if(bestVal<=alpha): # we need beta < alpha
                    brk = True
                    break
                beta = min(bestVal, beta)
                #########################
                #########################
                #########################
                new_Board = board
                new_Board[i][j] = 4

                value = minimax(new_Board, depth+1, alpha, beta, True)

                bestVal = min(bestVal, value)
                if(bestVal<=alpha):
                    brk = True
                    break
                beta = min(bestVal, beta)

        
        return bestVal

        
    


    
    


    

def findBestMovePlayer(board):

    if(TerminalState(board)):
        return "left"

    ret = ""
    bestScore = -1e9

    arr = []

    new_Board,dummy = move_left(board)
    k1 = minimax(new_Board, 0, -1e9, 1e15, True)
    print()
    print(f"left {k1}")
    if(k1>bestScore and dummy):
        ret = "left"
        bestScore = k1
        arr.clear()
        arr.append("left")

    
    

    new_Board,dummy = move_right(board)
    k2 = minimax(new_Board, 0, -1e9, 1e15, True)
    print(f"right {k2}")
    if(k2>bestScore and dummy):
        ret = "right"
        bestScore = k2
        arr.clear()
        arr.append("right")
    elif(k2==bestScore and dummy):
        arr.append("right")

    new_Board,dummy = move_up(board)
    k3 = minimax(new_Board, 0, -1e9, 1e15, True)
    print(f"up {k3}")
    if(k3>bestScore and dummy):
        ret = "up"
        bestScore = k3
        arr.clear()
        arr.append("up")
    elif(k3==bestScore and dummy):
        arr.append("up")

    new_Board,dummy = move_down(board)
    k4 = minimax(new_Board, 0, -1e9, 1e15, True)
    print(f"down {k4}")
    if(k4>bestScore and dummy):
        ret = "down"
        bestScore = k4
        arr.clear()
        arr.append("down")
    elif(k4==bestScore and dummy):
        arr.append("down")
    
    new_Board = board
    print(arr)
    ret = arr[random.randint(0,len(arr)-1)]

    return ret
