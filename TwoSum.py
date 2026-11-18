<<<<<<< HEAD
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
=======
#Two sum
def two_sum(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return [] 
>>>>>>> 7c737c195fac41cbb2c20b9f2191e5249cd4e889
