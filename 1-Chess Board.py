
def chess_board(n:int ,m:int):
    for row in range(n):
        for col in range(m):
            if(row%2 == 0 and col%2 == 0) or (row%2 == 1 and col%2 == 1):
                print("#" , end="")
            else:
                print("*", end="")
        print()


