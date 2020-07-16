'''
You have a landscape, in which puddles can form. You are given an array of
non-negative integers representing the elevation at each location. Return the
amount of water that would accumulate if it rains.

For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water
can get trapped here.
'''
def capacity(arr):
    len_arr = len(arr)
    count = 0
    updated = True
    while updated:
        index = 1
        updated = False
        start = -1
        current_arr = arr[:]
        while index < len_arr - 1:
            before = index - 1
            after = index + 1
            if arr[before] > arr[index] and arr[index] < arr[after]:
                count += 1
                updated = True
                start = -1
                current_arr[index] += 1
            elif arr[before] > arr[index] and arr[index] == arr[after]:
                if start == -1:
                    start = index
                current_arr[index] += 1
            elif arr[before] == arr[index] and start != -1 and arr[index] < arr[after]:
                count += 1 + index - start
                updated = True
                current_arr[index] += 1
            elif arr[before] == arr[index] and arr[index] == arr[after]:
                current_arr[index] += 1
            index+= 1
        arr = current_arr
    return count

print capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# 6
