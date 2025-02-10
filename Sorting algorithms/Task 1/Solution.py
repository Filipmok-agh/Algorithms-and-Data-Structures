from zad1testy import Node, runtests
# SortH Algorithm
# The algorithm first sorts the first k elements of the list using selection sort.
# Then, for each subsequent element, it finds the correct position in the first k elements and inserts it.
# This approach reduces the number of comparisons and swaps compared to a traditional insertion sort.
# Time complexity:
# - For k = 1: O(n)
# - For k = logn: O(n log n)
# - For k = n: O(n * (k-1)) because each element may need to be shifted by k-1 positions.

def SortH(head, k):
    g = Node()
    g.val = None
    g.next = head
    sorted_list = Node()
    sorted_tail = sorted_list
    sorted_list.val = None
    i = 0

    while i < k:
        prev = g
        p = g
        min_node = p.next
        cnt = 0
        while cnt <= k - i:
            if p.next.val < min_node.val:
                min_node = p.next
                prev = p
            p = p.next
            cnt += 1
        prev.next = prev.next.next
        sorted_tail.next = min_node
        sorted_tail = sorted_tail.next
        sorted_tail.next = None
        i += 1

    sorted_tail.next = g.next
    prev = sorted_list.next
    p = sorted_tail.next
    sorted_tail = sorted_tail.next

    while p.next != None:
        min_node = prev
        cnt = 0
        while cnt < k:
            cnt += 1
            if min_node.next.val > p.next.val:
                holder = p.next.next
                p.next.next = min_node.next
                min_node.next = p.next
                sorted_tail.next = holder
                break
            if cnt == k:
                sorted_tail = sorted_tail.next
                p = p.next
            min_node = min_node.next
        prev = prev.next

    return sorted_list.next

runtests( SortH, all_tests = True )
input("Press Enter to exit...")
