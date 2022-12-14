arr = [i for i in range(100000000)]
def sqrt(N):
    low = 0
    high = len(arr)-1
    while high >= low:
        mid = (high + low) // 2
        if (arr[mid])**2 == N:
            return mid
        elif (arr[mid])**2 > N:
            high = mid-1
        else:
            low = mid+1
    return False

from math import sqrt as sq
test_cases = [0,1,4,85248289,22297284,18939904,91107025,69122596,9721924,37810201,1893294144,8722812816,644398225]
answers = [int(sq(x)) for x in test_cases]

def checkValid():
    for i in range(len(test_cases)):
        if sqrt(test_cases[i]) == answers[i]:
            print("Check number {} passed".format(i+1))
        else:
            print("Check number {} failed".format(i+1))

checkValid()