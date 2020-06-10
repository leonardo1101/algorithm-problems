class Solution:
  def lengthOfLongestSubstring(self, s):
    #Table that holds the last index of the letter in the string
    aux_table = [0 for i in range(26)]
    max_lenght  = 0
    current_lenght = 0
    # Last substring start index
    last_index_started = 1
    a_ascii_value = 97

    for index in range(len(s)):
        ascii_value = ord(s[index]) - a_ascii_value
        if aux_table[ascii_value] < last_index_started:
            aux_table[ascii_value] = index + 1
            current_lenght +=1

            if max_lenght < current_lenght:
                max_lenght = current_lenght
        else:
            current_lenght = index - (aux_table[ascii_value] - 1)
            last_index_started = aux_table[ascii_value]
            aux_table[ascii_value] = index + 1
    
    return max_lenght
print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10
