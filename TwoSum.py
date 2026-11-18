# Made a small change

nums = [2,7,11,15]
target = 9
res=[]
n = len(nums)
def twoSum(nums, n):
    for i in range(n-1):
        for j in range(n):
            ans = nums[i]+nums[j]
            if ans==target:
                res.append(i)
                res.append(j)
                return res
print(twoSum(nums, n))