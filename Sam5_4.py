marks1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
marks2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
marks3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def correct_marks(marks):
    for mark in marks:
        if mark == 2:
            marks.remove(mark)
        if mark == 3:
            mark = 4
    return marks
if __name__ == '__main__':
    print(correct_marks(marks1))
    print(correct_marks(marks2))
    print(correct_marks(marks3))