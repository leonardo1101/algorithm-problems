'''
You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.
'''

def maximum_product_of_three(lst):
    len_lst = len(lst)
    two_minor_values = []
    three_max_value = []

    if len_lst < 3:
        return None

    for i in range(len_lst):
        # Get the 3 max values
        if len(three_max_value) < 3:
            three_max_value.append(lst[i])
            if len(three_max_value) == 3:
                three_max_value.sort()
        else:
            if three_max_value[2] < lst[i]:
                three_max_value[0] = three_max_value[1]
                three_max_value[1] = three_max_value[2]
                three_max_value[2] = lst[i]
            elif three_max_value[1] < lst[i]:
                three_max_value[0] = three_max_value[1]
                three_max_value[1] = lst[i]
            elif three_max_value[0] < lst[i]:
                three_max_value[0] = lst[i]

        # Get the 2 min values
        if len(two_minor_values) < 2:
            two_minor_values.append(lst[i])
            if len(two_minor_values) == 2:
                two_minor_values.sort()
        else:
            if two_minor_values[0] > lst[i]:
                two_minor_values[1] = two_minor_values[0]
                two_minor_values[0] = lst[i]
            elif two_minor_values[1] > lst[i]:
                two_minor_values[1] = lst[i]

    mul_1 = two_minor_values[0] * two_minor_values[1] * three_max_value[2]
    mul_2 = three_max_value[0] * three_max_value[1] * three_max_value[2]

    if mul_1 < mul_2:
        return mul_2
    else:
        return mul_1

print maximum_product_of_three([-4, -4, 2, 8])
# 128
print maximum_product_of_three([-4, -4, -2, -3])
# -24
