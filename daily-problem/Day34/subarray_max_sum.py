'''
Contiguous Subarray with Maximum Sum

You are given an array of integers. Find the maximum sum of all possible
contiguous subarrays of the array.
'''

def max_subarray_sum(arr):
    last_sum = 0
    len_arr = len(arr)
    max_sum = None

    for i in range(len_arr):
        if arr[i] < 0:
            last_sum += arr[i]
        else:
            if last_sum < 0:
                last_sum = arr[i]
            else:
                last_sum += arr[i]

        if max_sum < last_sum or max_sum == None:
            max_sum = last_sum
    return max_sum



print max_subarray_sum([34, -50, 42, 14, -5, 86])
# 137
