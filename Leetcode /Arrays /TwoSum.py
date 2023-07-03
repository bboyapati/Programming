"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

'''
Time Complexity: O(n)

Use dictionary to store previously encountered numbers as keys and their indices as values 
Iterate through nums using enumerate function
For each element n at index i, calculate difference between target and n
Check if difference exists as key in dictionary to find complement as n + complement = target
'''
