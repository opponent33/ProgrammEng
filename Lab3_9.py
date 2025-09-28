value = 0
for i in range(0,1):
    for j in range(0,1):
        for z in range(0,1):
            if not(i or j) or (i == j):
                print(i , j , z)
