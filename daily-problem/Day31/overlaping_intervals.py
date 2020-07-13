'''
Merge Overlapping Intervals

You are given an array of intervals - that is, an array of tuples (start, end).
The array may not be sorted, and could contain overlapping intervals.
Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).
'''

def merge(intervals):
    dict_intervals = {}
    len_number_inter = len(intervals)
    list_overlapping = []
    intervals.sort()

    index = 0
    while index < len_number_inter:
        start = intervals[index][0]
        max_end = intervals[index][1]
        index += 1
        if index < len_number_inter:
            while start <= intervals[index][0] and intervals[index][0] <= max_end:
                if max_end < intervals[index][1]:
                    max_end = intervals[index][1]
                index += 1
        index -= 1
        list_overlapping.append((start, max_end))
        index += 1
    return list_overlapping

print merge([(1, 3), (5, 8), (4, 10), (20, 25)])
# [(1, 3), (4, 10), (20, 25)]
