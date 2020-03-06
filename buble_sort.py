# # Ascending order
# def buble_sort(lst):
#     for i in range(len(lst)-1, 0, -1): # time complexity 0(n^2), space complexity 0(1)
#         for j in range(i):
#             if lst[j] > lst[j+1]:
#                 temp = lst[j]
#                 lst[j] = lst[j+1]
#                 lst[j+1] = temp

# lst = [4, 2, 8, 9, 1, 3, 10]
# buble_sort(lst)
# print(lst)


# Decending order
def buble_sort(lst):
    for i in range(len(lst)-1, 0, -1): # time complexity 0(n^2), space complexity 0(1)
        for j in range(i):
            if lst[j] < lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

lst = [4, 2, 8, 9, 1, 3, 10]
buble_sort(lst)
print(lst)
