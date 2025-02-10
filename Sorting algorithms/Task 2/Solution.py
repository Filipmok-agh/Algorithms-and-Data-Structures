from zad2testy import runtests
# The program creates an array of size 'p' that contains the first 'p' elements.
# It sorts the array using heapsort, then selects the (p-k)-th element, as this is the k-th largest element.
# This element is added to the sum, and the element at the beginning of the range is removed using binary search.
# Finally, a new element is inserted at the appropriate position in the array using binary insert.
# Time complexity is:O(n*log(p)).
def ksum(T, k, p):
    def copy_elements(T, size):
        copy = [None] * size
        for i in range(size):
            copy[i] = T[i]
        return copy

    def find_element_index(T, target):
        n = len(T)
        def search(left, right):
            i = (left + right) // 2
            if T[i] == target:
                return i
            elif T[i] > target:
                return search(left, i - 1)
            else:
                return search(i + 1, right)

        return search(0, n - 1)

    def binary_insert_position(T, target):
        n = len(T)
        
        def search(left, right):
            if left == right:
                if T[left] > target:
                    return left
                else:
                    return left + 1
            if left > right:
                return left
            i = (left + right) // 2
            if T[i] > target:
                return search(left, i - 1)
            elif T[i] < target:
                return search(i + 1, right)
            else:
                return i

        return search(0, n - 1)

    def heapify(T, n, i):
        left = (2 * i) + 1
        largest = i
        right = (2 * i) + 2
        if left < n and T[left] > T[largest]:
            largest = left
        if right < n and T[right] > T[largest]:
            largest = right
        if largest != i:
            T[i], T[largest] = T[largest], T[i]
            heapify(T, n, largest)

    def build_max_heap(T):
        n = len(T)
        parent = (n - 1) // 2
        for i in range(parent, -1, -1):
            heapify(T, n, i)

    def heapsort(T):
        n = len(T)
        build_max_heap(T)
        for i in range(n - 1, 0, -1):
            T[i], T[0] = T[0], T[i]
            heapify(T, i, 0)

    selected_elements = copy_elements(T, p)
    heapsort(selected_elements)

    total_sum = 0
    n = len(T)
    
    for i in range(n - p):
        out_element = T[i]
        total_sum += selected_elements[p - k]
        selected_elements.pop(find_element_index(selected_elements, out_element))
        selected_elements.insert(binary_insert_position(selected_elements, T[i + p]), T[i + p])
    
    total_sum += selected_elements[p - k]
    return total_sum

runtests(ksum, all_tests=True)
input("Press Enter to exit...")
