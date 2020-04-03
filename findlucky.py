def findlucky(arr):
    import collections

    count = collections.Counter(arr)
    luckynum = [-1]
    for i in count.keys():
        if i==count.get(i):
            luckynum.append(i)

    return max(luckynum)

print(findlucky([1,2,3,3,3]))
