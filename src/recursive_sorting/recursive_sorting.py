# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a_i = 0
    b_i = 0
    for i in range(elements):
        # print(f'a,b: {a_i}, {b_i}, {merged_arr}')
        if a_i >= len(arrA):
            merged_arr[i] = arrB[b_i]
            b_i += 1
        elif b_i >= len(arrB):
            merged_arr[i] = arrA[a_i]
            a_i += 1
        elif arrA[a_i] < arrB[b_i]:
            merged_arr[i] = arrA[a_i]
            a_i += 1
        else:
            merged_arr[i] = arrB[b_i]
            b_i += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
"""
# (base case) if the array is empty or len(arr) == 1, return
# split the arrays into half ==> arr[1], arr[2]
# sort each half ==> recursively!
# merge them back together : compare the first values fo each array, add smaller to result
"""

def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        #split
        mid = len(arr) // 2
        small = arr[:mid]
        large = arr[mid:]
        left = merge_sort(small)
        right = merge_sort(large)
        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


def quicksort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    smaller = quicksort(smaller)
    larger = quicksort(larger)
    return smaller + [pivot] + larger