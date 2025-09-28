even_arr = [2, 4, 6, 8, 9]
flag = False
for value in even_arr:
    if value % 2 == 1:
        flag = True

if flag:
    print("THERE IS UNEVEN NUMBER IN ARRAY")
else:
    print("ALL NUMBERS ARE EVEN")