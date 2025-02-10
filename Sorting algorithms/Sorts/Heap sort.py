# Heap Sort Algorithm
# This algorithm sorts an array by first building a max heap and then extracting the maximum element
# and placing it at the end of the array repeatedly.
# Time complexity: O(n log n)

def left_child(x):
    return 2 * x + 1

def right_child(x):
    return 2 * x + 2

def parent(x):
    return (x - 1) // 2

def heapify(arr, n, i):
    left = left_child(i)
    right = right_child(i)
    largest = i
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(parent(n - 1), -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
