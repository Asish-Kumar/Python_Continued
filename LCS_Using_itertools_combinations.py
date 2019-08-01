from itertools import combinations as comb


def get_lcs(list1, list2) -> []:
    length = min(len(list1), len(list2))

    while length > 0:
        combinations_list1 = list(comb(list1, length))
        combinations_list2 = list(comb(list2, length))
        for x in combinations_list1:
            if x in combinations_list2:
                return list(x)

        length -= 1
    return []


input_list1 = list(input("Enter elements of first sequence:"))
input_list2 = list(input("Enter elements of second sequence:"))

lcs = get_lcs(input_list1, input_list2)
print("LCS is ", "".join(x for x in lcs))
