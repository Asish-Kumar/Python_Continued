list1 = []
for _ in range(int(input("Enter number of elements: "))):
    list1.append(int(input()))  # take list elements from user input

for i in range(0, len(list1)-1):
    for j in range(0, len(list1)-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]  # swap

print(list1)
