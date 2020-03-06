# # Ascending order
# def selection_sort(lst):
#     for i in range(len(lst)):
#         minpos = i

#         for j in range(i+1, len(lst)):   # time complexity 0(n2)
#             if lst[j] < lst[minpos]:
#                 minpos = j
        
#         temp = lst[i]
#         lst[i] = lst[minpos]
#         lst[minpos] = temp

# lst = [5, 2, 7, 1, 9, 10, 4, 16, 15, 1, 13, 19]
# selection_sort(lst)
# print(lst)


# Decending order
def selection_sort(lst):
    for i in range(len(lst)-1):
        maxpos = i

        for j in range(i+1, len(lst)):   # time complexity 0(n2)
            if lst[j] > lst[maxpos]:
                maxpos = j
        
        temp = lst[i]
        lst[i] = lst[maxpos]
        lst[maxpos] = temp
        
lst = [5, 2, 7, 1, 9, 10, 4, 16, 15, 1, 13, 19]
selection_sort(lst)
print(lst)

