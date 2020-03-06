pos = 0
def binary_search(lst, n):
    lower = 0
    upper = len(lst) - 1

    while lower <= upper:               # Space complexity 0(1), time complexity 0(logn)
        mid = (lower + upper) // 2

        if lst[mid] == n:
            globals()['pos'] = mid
            return True

        else:            
            if lst[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1

lst = [3, 4, 5, 6, 7, 8, 9, 10]
n = 6

if binary_search(lst, n):
    print("Found", pos+1)
else:
    print("Not Found")