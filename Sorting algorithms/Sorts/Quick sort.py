# QuickSort Algorithm
# The QuickSort algorithm sorts an array by choosing a pivot and partitioning the array such that
# elements less than the pivot are on the left side, and elements greater than the pivot are on the right side.
# This is followed by recursively sorting the left and right subarrays. The average time complexity is O(n log n),
# but in the worst case (when the pivot selection is poor), the time complexity is O(n^2).

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def quicksort(arr, left, right):
    while left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)
        left = pivot_index + 1
