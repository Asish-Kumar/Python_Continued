"""
A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
example input : UDDDUDUU
"""
def countingValleys(n, s):
    result = 0
    k = 0
    start = False
    for i in range(n):
        if k < 0:
            start = True
        else:
            start = False
        if s[i] == 'D':
            k -= 1
        else:
            k += 1
        print(start, k)
        if start and k==0:
            result += 1

    return result


s = input("Enter U and D combinations: ")
print(countingValleys(len(s), s))
