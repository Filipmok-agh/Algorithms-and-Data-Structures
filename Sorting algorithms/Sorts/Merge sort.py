# Merge Sort on a singly linked list.
# The algorithm splits the list into two halves, recursively sorts them, and then merges them.
# Time complexity: O(n log n)

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def merge_sorted_lists(list1, list2):
    tmp_node = Node()
    current_node = tmp_node
    
    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next
        current_node = current_node.next

    if list1 is None:
        current_node.next = list2
    elif list2 is None:
        current_node.next = list1

    return tmp_node.next

def split_list(head):
    while head.next is not None and head.value <= head.next.value:
        head = head.next
    
    second_half = head.next
    head.next = None

    return second_half

def get_last_node(head):
    while head is not None and head.next is not None:
        head = head.next
    return head

def merge_sort(head):
    tmp_node = Node()
    tmp_node.next = head
    current_node = tmp_node

    while True:
        second_half = split_list(current_node.next)
        if second_half is None:
            break
        first_half = split_list(second_half)

        merged_list = merge_sorted_lists(current_node.next, second_half)

        if first_half is None:
            current_node.next = merged_list
            break
        last_node = get_last_node(merged_list)
        last_node.next = first_half

        current_node = get_last_node(merged_list)

    return tmp_node.next
