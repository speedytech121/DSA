def majority_element(arr):
    d = {}
    res = majority = 0

    for elem in arr:
        d[elem] = 1 + d.get(elem, 0)
        if d[elem] > majority:
            res = elem
            majority = d[elem]
    return res


# n/3 times
def majority_nbythree(arr):
    d = {}
    limit = len(arr) // 3
    li = set()
    for elem in arr:
        d[elem] = 1 + d.get(elem, 0)
        if d[elem] > limit:
            li.add(elem)
    return list(li)


arr = [6, 5, 5]
print(majority_element(arr))

arr = [1, 2]
print(majority_nbythree(arr))
arr = [1]
print(majority_nbythree(arr))
arr = [3, 2, 3]
print(majority_nbythree(arr))
