


def multiple_table(n:int , m:int):
        
    for row in range(1,n+1):
        for col in range(1,m+1):
            r = row*col
            print(r, end="  ")
        print()


multiple_table(4,4)