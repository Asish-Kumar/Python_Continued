# from itertools import permutations as pt
#
# def is_valid(asgnmt : list):
#     dct = dict()
#     prev_key = -1
#     for cur in asgnmt:
#         if prev_key != cur:
#             try:
#                 dct[cur] += 1
#                 return False
#             except KeyError:
#                 dct[cur] = 1
#                 prev_key = cur
#     return True
#
#
# def main():
#     P, D = [int(x) for x in input().split()]
#
#     ar = []
#     if P > D:
#         for i in range(P):
#             if i < D:
#                 j=i
#             ar.append(j)
#     else:
#         for i in range(D):
#             ar.append(i)
#
#     #get all the possible doctors assignments
#     perm = list(pt(ar, P))
#
#     #now remove invalid doctor assignment
#     valids = list(filter(is_valid, perm))
#
#     #read the efforts input
#     efforts = []
#     for i in range(1, D+1):
#         efforts.append([int(x) for x in input().split()])
#
#     #now find the minimum cost in all the valids
#     min_ = 99999999999
#     for valid in valids:
#         cur_cost = 0
#         for patient in range(P):
#             assigned_doc = valid[patient]
#             cur_cost += efforts[assigned_doc][patient]
#         if cur_cost < min_:
#             min_ = cur_cost
#
#     print(min_)
#
#
#
# main()
#
#
#
# """
# 10 5
# 1 99 1 1 1 1 1 8 1 1
# 2 1 1 1 1 33 2 4 5 11
# 33 1 1 1 1 42 5 44 3 1
# 3 2 5 4 5 6 7 4 7 8
# 6 7 8 9 6 4 3 2 4 5
#
#
# 2 1 1 1 1 1 1 2 3 1 = 14
#
# """
l1 =[1,2,3]
l2 = [4,5]
l1.extend(l2)
print(l1)