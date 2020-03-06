def insertion_sort(lst):
    for i in range(1, len(lst)): # time complexity 0(n^2)
        item = lst[i]

        j = i - 1
        while j >= 0 and lst[j] > item:
            lst[j+1] = lst[j]
            j = j - 1
            lst[j+1] = item

lst = [5, 4, 3, 2, 1, 6]
insertion_sort(lst)
print(lst)
