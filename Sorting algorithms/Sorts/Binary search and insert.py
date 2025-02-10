# Function to find the index of an element using binary search.
# Time complexity: O(log n)

def find_element_index(sorted_list, target):
    n = len(sorted_list)

    def binary_search(left, right):
        middle = (left + right) // 2
        if sorted_list[middle] == target:
            return middle
        elif sorted_list[middle] > target:
            return binary_search(left, middle - 1)
        else:
            return binary_search(middle + 1, right)

    return binary_search(0, n - 1)

# Function to find the index where the element can be inserted.
# Time complexity: O(log n)

def find_insert_position(sorted_list, target):
    n = len(sorted_list)

    def binary_search(left, right):
        if left == right:
            if sorted_list[left] > target:
                return left
            else:
                return left + 1
        if left > right:
            return left
        middle = (left + right) // 2
        if sorted_list[middle] > target:
            return binary_search(left, middle - 1)
        elif sorted_list[middle] < target:
            return binary_search(middle + 1, right)
        else:
            return middle

    return binary_search(0, n - 1)
