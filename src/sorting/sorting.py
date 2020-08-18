# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    a = 0
    b = 0
    while i < elements:
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        else:
            if arrA[a] < arrB[b]:
                merged_arr[i] = arrA[a]
                a += 1
            else:
                merged_arr[i] = arrB[b]
                b += 1
        i += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
import math
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr
    else:
        mid = math.floor(len(arr) / 2)
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

