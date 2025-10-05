from random import randint

def casino():
    throw = randint(1, 6)
    if throw >= 5:
        print("You are win!!!")
    elif throw <= 2:
        print("You are lose!!!")
    else:
        casino()

if __name__ == '__main__':
    casino()