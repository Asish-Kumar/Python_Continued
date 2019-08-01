"""
Question is:
Given a string of brackets (, ), {, }, [, ], find the position in the string where the orders of brackets breaks.
Input string will only contain brackets
"""
s = input()
bracket_values = [0, 0, 0]
brackets = {"(": [0, 1],
            ")": [0, -1],
            "{": [1, 1],
            "}": [1, -1],
            "[": [2, 1],
            "]": [2, -1]}
for i in range(len(s)):
    bracket_values[brackets[s[i]][0]] += brackets[s[i]][1]
    if bracket_values[brackets[s[i]][0]] < 0:
        print(i)
        exit(0)
if not ([0, 0, 0] == bracket_values):
    print(len(s))
else:
    print(-1)
