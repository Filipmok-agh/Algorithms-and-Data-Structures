# Counting Sort for Integers
# This algorithm sorts an array of integers where the values range from 0 to k-1.
# It uses a counting technique to determine the number of occurrences of each element,
# and then computes the position of each element in the sorted order based on these counts.
# Time Complexity: O(n + k)

def counting_sort_integers(arr, k):
    n = len(arr)
    output = [0 for _ in range(n)]
    count = [0 for _ in range(k)]

    for num in arr:
        count[num] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    for i in range(n):
        arr[i] = output[i]

# Counting Sort for Strings
# This version of counting sort works for sorting strings.
# It sorts a string of lowercase letters by counting the occurrences of each character,
# mapping the characters to their corresponding positions based on their ASCII values.
# Time Complexity: O(n + k)

def counting_sort_string(s, k):
    T = list(s)
    n = len(T)
    output = [0 for _ in range(n)]
    count = [0 for _ in range(k)]

    for char in T:
        count[ord(char) - 97] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        output[count[ord(T[i]) - 97] - 1] = T[i]

    return ''.join(output)
