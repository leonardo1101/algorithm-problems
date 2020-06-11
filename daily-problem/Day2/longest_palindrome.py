class Solution:
    # Checks if the word is a Palindrome
    def isPalindrome(self, s):
        i = 0
        j = 0
        for i in range(len(s)):
            j = len(s) - i - 1
            if j < i:
                break
            if s[i] != s[j]:
                return False
        return True

    def longestPalindrome(self, s):
        # List that will contain all combination words
        combination_list = [s]
        max_len = len(s)
        
        while (max_len != 1):
            new_combination = []
            # The for will check each word
            for index in range(len(combination_list)):
                word = combination_list[index]
                if Solution().isPalindrome(word):
                    return word
                if max_len > 2:
                    # Each new word will be formed removing the last and first letter from the string
                    new_combination.append(word[:-1])
                    new_combination.append(word[1:])
            combination_list = new_combination
            max_len-= 1
        # If there isn't a palindrome the first letter will be showed
        return s[0]

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
