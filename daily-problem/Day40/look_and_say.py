'''
Look and Say Sequence

A look-and-say sequence is defined as the integer sequence beginning with a
single digit in which the next term is obtained by describing the previous term.
An example is easier to understand:

Each consecutive value describes the prior value.

1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's.
'''

def lookSaySequence(term):

    if term == 1:
        return "1"

    prev_sequence = lookSaySequence(term - 1)

    len_sequence = len(prev_sequence)
    index = 1
    current_number = prev_sequence[0]
    count_number = 1
    sequence = ""

    while index < len_sequence:
        if prev_sequence[index] != current_number:
            sequence += "{0}{1}".format(count_number, current_number)
            count_number = 0
            current_number = prev_sequence[index]
        index += 1
        count_number += 1
    sequence += "{0}{1}".format(count_number, current_number)
    return sequence

print(lookSaySequence(5))
# 111221

print(lookSaySequence(5))
# 312211
