# TO-DO: Complete the selection_sort() function below 
"""
1. Start with current index = 0
2. For all indices EXCEPT the last index:
    - len(n-1) bc after the sort, the one remaining will be the largest
    a. Loop through elements on right-hand-side of current index and find the smallest element
    b. Swap the element at current index with the smallest element found in above loop
"""

import math

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index] 
    return arr


# TO-DO:  implement the Bubble Sort function below
"""
1. Loop through your array
    - Compare each element to its neighbor
    - If elements in wrong position (relative to each other, swap them)
2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
"""
def bubble_sort( arr ):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                # print(f'i: {i}, j: {j}, {arr}')
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


# STRETCH: implement the Count Sort function below
"""
Count sort : based on keys between a specific range
    - linear time : O(n) // faster 
    - restricted inputs : only works when the range of items in the input is know ahead of time
    - space cose : O(n)
"""
def count_sort( arr, maximum=-1 ):
    # count the number of times each value appears
    counts = [0] * (maximum + 1) # n=5 [0, 0, 0, 0, 0, 0]
    for item in arr:
        counts[item] += 1
    total = 0
    for i in range(1, len(counts)):
        counts[i], total = total, counts[i] + total
    sorted_list = [None] * len(arr)
    for item in arr:
        sorted_list[counts[item]] = item
        counts[item] += 1
    return arr


# insertion sort
"""
Time complexity : O(n^2) 
    - "in place" (not using extra memory || not creating new array)
Space complexity : O(1)
"""
def insertion_sort( arr ):
    # Divide your hand into sorted on the left and unsorted on the right
    # arr[0] = sorted || start arr[1] unsorted
    # go card by card and move them into place
    # loop through all elements in unsorted
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i # j == sliding index
        print(f'i is {i}, j = {j} temp = {temp}')
        # shift sorted to the right until correct position found
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1] # slide over one element
            j -= 1
            arr[j] = temp
    return arr