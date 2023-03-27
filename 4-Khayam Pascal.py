

n=int(input())

final_nums = []

for i in range(n):
    row_num=[]
    for j in range(i+1):
        if j == 0 or j == i:
            row_num.append(1)
        else:
            row_num.append(final_nums[i-1][j] + final_nums[i-1][j-1])

    final_nums.append(row_num)

for row in final_nums:
    for col in row:
        print(col, end=" ")
    print()
        

