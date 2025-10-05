
def aggregate(*args):
    sum = 0
    count = 0
    for arg in args:
        sum += arg
        count += 1
    agg = sum / count
    return agg

if __name__ == '__main__':

    print(aggregate(1, 2, 4, 5))