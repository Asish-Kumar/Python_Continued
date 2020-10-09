from itertools import combinations
# this method also counts any repetitions of value, so read in the question carefully


def get_length(l: list) -> int:
    try:
        i = 0
        while True:
            _ = l[i]
            i += 1
    except IndexError:
        return i


s = [int(x) for x in input("Enter a space seperated integer sequence: ").split()]
break_ = False
for j in range(get_length(s), 1, -1):
    comb_ = combinations(s, j)

    for comb in comb_:
        if sorted(comb) == list(comb):
            print(comb, "Length is", j)
            break_ = True
            break
    if break_:
        break

