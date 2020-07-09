'''
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
    def moveZeros(self, nums):
        stack = []
        number_nums = len(nums)
        # Using a list we can save the index when is zero and when isn't equal
        # to zero we change the values by getting the first occurrence of zero
        for i in range(number_nums):
            if nums[i] == 0:
                stack.append(i)
            else:
                if stack:
                    avaliable_index = stack.pop(0)
                    aux = nums[avaliable_index]
                    nums[avaliable_index] = nums[i]
                    nums[i] = aux
                    stack.append(i)

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
print(nums)
Solution().moveZeros(nums)
print(nums)
