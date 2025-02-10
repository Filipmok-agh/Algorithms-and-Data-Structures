# Radix Sort Algorithm for Strings
# Radix Sort works by sorting elements based on individual digits (or characters in the case of strings).
# It processes each character of the strings starting from the least significant one and performs counting sort
# on each character.
# Time complexity: O(n * k)

def radix_sort(arr, max_len):
    n = len(arr)
    temp = [0 for _ in range(n)]
    count = [0 for _ in range(26)]
    max_len -= 1

    while max_len >= 0:
        for string in arr:
            if len(string) <= max_len:
                count[0] += 1
            else:
                count[ord(string[max_len]) - 97] += 1

        for i in range(1, 26):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            if len(arr[i]) <= max_len:
                temp[count[0] - 1] = arr[i]
                count[0] -= 1
            else:
                temp[count[ord(arr[i][max_len]) - 97] - 1] = arr[i]
                count[ord(arr[i][max_len]) - 97] -= 1

        max_len -= 1
        count = [0 for _ in range(26)]

        for i in range(n):
            arr[i] = temp[i]

        temp = [0 for _ in range(n)]
