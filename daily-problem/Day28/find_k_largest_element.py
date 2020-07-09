'''
Given a list, find the k-th largest element in the list.

Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
'''

def k_largest_element(nums, k):
    nums.sort()
    size_nums = len(nums)

    if k > size_nums or k <= 0:
        return None
    else:
        return nums[size_nums - k]

nums = [3, 5, 2, 4, 6, 8]
print(k_largest_element(nums, 3))
