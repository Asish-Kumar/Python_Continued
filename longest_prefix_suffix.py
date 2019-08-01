"""
Question is:
Longest prefix which is also suffix:
Given a string s, find length of the longest prefix which is also suffix. The prefix and suffix should not overlap.
"""
s = input()
length = len(s)
count_ = 0
k = 1
while length > 1:
    length -= 2
    if s[:k] == s[-k:]:
        count_ = k
    k += 1
print(count_)