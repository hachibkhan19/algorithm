pos = 0
def linear_search(lst, n):

    for i in range(len(lst)):          # space complexity 0(1), time complexity(n)        
        if lst[i] == n:
            globals()['pos'] = i       # best case complexity 0(1), worst case complexity 0(n)
            return True                # average case complexity 0(n)
    return False

lst = [3, 1, 5, 6, 10]
n = 1
if linear_search(lst, n):
    print("Found", pos+1)
else:
    print("Not Found")
    