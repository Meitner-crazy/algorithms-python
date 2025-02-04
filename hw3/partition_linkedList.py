# pylint: skip-file
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def partitionLinkedList(head):
    '''
    1. The first node of the original linked list is chosen as a pivot.
    2. All nodes with values less than the pivot come before the pivot node.
    3. All nodes with values equal to the pivot (including the pivot node) come next.
    4. All nodes with values greater than the pivot come after.
    '''
    if not head or not head.next:
        return head

    cur = head.next
    pivot = cur.val
    less_than_pivot = Node(-1)
    equal_to_pivot = Node(-1)
    greater_than_pivot = Node(-1)

    less_node = less_than_pivot
    greater_node = greater_than_pivot
    equal_node = equal_to_pivot

    while cur:
        if cur.val < pivot:
            less_node.next=cur
            less_node=less_node.next
        elif cur.val > pivot:
            greater_node.next=cur
            greater_node=greater_node.next
        else:
            equal_node.next=cur
            equal_node=equal_node.next
        cur=cur.next

    less_node.next = equal_to_pivot.next
    equal_node.next = greater_than_pivot.next
    greater_node.next = None

    head.next = less_than_pivot.next if less_than_pivot.next else greater_than_pivot.next
    return head



# Helper functions for testing
def array_to_linked_list(arr):
    head = Node("head")
    cur = head
    for i in arr:
        cur.next = Node(i)
        cur = cur.next
    return head

def print_linked_list(head):
    if head.val == "head":
        print("head", end=" -> ")
    else:
        raise Exception("The linked list is malformed")
    cur = head.next
    while cur:
        if not cur.next:
            print(cur.val, end="")
        else:
            print(cur.val, end=" -> ")
        cur = cur.next
    print()

# sample test cases
LL = array_to_linked_list([1])
print_linked_list(partitionLinkedList(LL)) # head -> 1
LL = array_to_linked_list([1, 1, 1])
print_linked_list(partitionLinkedList(LL)) # head -> 1 -> 1 -> 1
LL = array_to_linked_list([2, 1, 3, 2, 1, 3])
print_linked_list(partitionLinkedList(LL)) # head -> 1 -> 1 -> 2 -> 2 -> 3 -> 3
LL = array_to_linked_list([2, 4, 5, 7])
print_linked_list(partitionLinkedList(LL)) # head -> 2 -> 4 -> 5 -> 7
LL = array_to_linked_list([7, 4, 5, 2])
print_linked_list(partitionLinkedList(LL)) # head -> 4 -> 5 -> 2 -> 7
LL = array_to_linked_list([6, 2, 7, 9, 3, 1, 5, 2, 6, 7, 3])
print_linked_list(partitionLinkedList(LL))
# head -> 2 -> 3 -> 1 -> 5 -> 2 -> 3 -> 6 -> 6 -> 7 -> 9 -> 7
LL = array_to_linked_list([-6, 2, 7, 9, 3, -1, 5, 2, 6, 7, 3])
print_linked_list(partitionLinkedList(LL))
# head -> -6 -> 2 -> 7 -> 9 -> 3 -> -1 -> 5 -> 2 -> 6 -> 7 -> 3
LL = array_to_linked_list([6, 2, 7, 9, 3, -1, 5, 2, 6, 7, 3])
print_linked_list(partitionLinkedList(LL))