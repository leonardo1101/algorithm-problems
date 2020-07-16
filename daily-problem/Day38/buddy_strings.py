'''
Buddy Strings
Given two strings A and B of lowercase letters, return true if and only if we
can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true
'''

class Solution:
    def buddyStrings(self, A, B):
        repeated_letter = {}
        has_repeated_letter = False
        num_diff_letter = 0
        original_letter = []
        needed_letter = []

        len_a = len(A)
        len_b = len(B)

        if len_a != len_b:
            return False

        for i in range(len_a):
            if A[i] != B[i]:
                num_diff_letter += 1
                original_letter.append(A[i])
                needed_letter.append(B[i])
            if A[i] not in repeated_letter:
                repeated_letter[A[i]] = 0
            repeated_letter[A[i]] += 1
            if repeated_letter[A[i]] > 1:
                has_repeated_letter = True

        if num_diff_letter == 2:
            if original_letter[0] == needed_letter[1] and original_letter[1] == needed_letter[0]:
                return True
            else:
                return False
        elif num_diff_letter == 0 and has_repeated_letter:
            return True

        return False

print Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb')
# True
print Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb')
# False
