"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
"""
Create a set as it can't have duplicate items
Iterate through through array
if integer in array is also in set, duplicate found and return TRUE
Otherwise, add the element to the list
"""

    








