def two_sum(nums, target):
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic:
            return [dic[complement], i]
        dic[num] = i
    return []
num1 = [2, 7, 11, 15]
target1 = 9
res = two_sum(num1, target1)

print(res)  # 0, 1