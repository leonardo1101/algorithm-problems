class Solution:
  def minSubArrayLenRec(self, nums, s):
    result1 = 0
    result2 = 0
    
    if s <= 0:
      return 0

    if not nums:
      return -1
    result1 = Solution().minSubArrayLenRec(nums[1:], s - nums[0])
    result2 = Solution().minSubArrayLenRec(nums[1:], s)

    if result1 == -1 and result2 == -1:
      return -1
    elif result1 == -1:
      return result2
    elif result2 == -1:
      return result1 + 1
    elif result1 + 1 <= result2:
      return result1 + 1
    else:
      return result2      

  def minSubArrayLen(self, nums, s):
    res = Solution().minSubArrayLenRec(nums, s)
    if res == -1:
      return 0
    else:
      return res

print Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7)
