# Selection Sort for Linked List
# The selection sort algorithm sorts a linked list by repeatedly selecting the minimum element from the unsorted part
# and moving it to the sorted part.
# Time complexity: O(n^2)

class Node:
    def __init__(self):
        self.val = None
        self.next = None

def selection_sort(head):
    dummy = Node()
    dummy.val = None
    dummy.next = head
    sorted_list = Node()
    sorted_list.val = None
    sorted_tail = sorted_list

    while dummy.next is not None:
        current = dummy
        min_node = current
        while current.next is not None:
            if current.next.val < min_node.next.val:
                min_node = current
            current = current.next
        sorted_tail.next = min_node.next
        min_node.next = min_node.next.next
        sorted_tail = sorted_tail.next

    sorted_tail.next = None
    return sorted_list.next
