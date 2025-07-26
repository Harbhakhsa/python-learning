# 1. Two Sum - Easy
# LeetCode Link: https://leetcode.com/problems/two-sum/

nums = [0,1,2,3,4,5,6,7,8,9]
target = 9 # just for example you can take any number or even input from user
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):    #i+1 is used so that no two answer is repeated.
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])
