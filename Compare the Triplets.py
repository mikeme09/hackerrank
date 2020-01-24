def compareTriplets(a,b):

    alice = 0
    bob = 0

    # INDEX 0
    if a[0] > b[0]:
        alice += 1
    elif a[0] < b[0]:
        bob += 1
    elif a[0] == b[0]:
        pass

    # INDEX 1
    if a[1] > b[1]:
        alice += 1
    elif a[1] < b[1]:
        bob += 1
    elif a[1] == b[1]:
        pass

    #INDEX 2
    if a[2] > b[2]:
        alice += 1
    elif a[2] < b[2]:
        bob += 1
    elif a[2] == b[2]:
        pass

    return result


#a = list(map(int, input('Enter ').rstrip().split()))
#b = list(map(int, input('Enter ').rstrip().split()))

if __name__ == '__main__':


    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    compareTriplets(a,b)
