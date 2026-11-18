arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]
res=[]
for num in arr1:
    if num not in res:
        res.append(num)
for num in arr2:
    if num not in res:
        res.append(num)
print(sorted(res))