def lcs_recursion(list1, list2):
    if not list1 or not list2:  # in case both the lists are empty
        return []
    head1, tail1, head2, tail2 = list1[0], list1[1:], list2[0], list2[1:]

    if head1 == head2:
        return [head1] + lcs_recursion(tail1, tail2)
    else:
        return max(lcs_recursion(list1, tail2), lcs_recursion(tail1, list2), key=len)


print(lcs_recursion([1, 2, 3, 4, 5], [2, 1, 2, 4, 5]))
