from math import sqrt
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

trg_list = []
one = sorted(one)
two = sorted(two)
three = sorted(three)

for i in range(0 , len(one)):
    if (one[i] < two[i] + three[i]) and (two[i] < one[i] + three[i]) and (three[i] < two[i] + one[i]):
        perimetr = (one[i] + two[i] + three[i])/2
        square = sqrt(perimetr * (perimetr - one[i])*(perimetr - two[i])*(perimetr - three[i]))
        trg_list.append([one[i], two[i], three[i], square])
print (max(trg_list))
print (min(trg_list))
