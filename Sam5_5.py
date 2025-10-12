list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def list_to_set(list):
    answer = set(list)
    for i in list:
        answer.add(i)
        for y in range(2, list.count(i)+1):
            answer.add(str(i)* y)
    return answer
if __name__ == "__main__":
    print(list_to_set(list_1))
    print(list_to_set(list_2))
    print(list_to_set(list_3))