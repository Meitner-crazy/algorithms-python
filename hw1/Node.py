# pylint: skip-file
class Node:
    #class for 
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def insertionSort(head):
     ## complete this function ##
    if not head or not head.next:
        return
    
    dummy = Node("dummy")
    cur = head.next
    prev = dummy
    next_node = None

    while cur:
        next_node = cur.next
        while prev.next and prev.next.val < cur.val:
            prev = prev.next

        cur.next = prev.next
        prev.next = cur
        prev = dummy
        cur = next_node

    head.next = dummy.next

# Helper functions for testing
def array_to_linked_list(arr):
    head = Node("head")
    cur = head
    for a in arr:
        cur.next = Node(a)
        cur = cur.next
    return head


def print_linked_list(head):
    print("head", end=" -> ")
    cur = head.next
    while cur != None:
        if not cur.next:
            print(cur.val, end="")
        else:
            print(cur.val, end=" -> ")
        cur = cur.next
    print()


# Sample test cases (Please add more test cases)
print("--------Insertion Sort--------------")
head = array_to_linked_list([1])
insertionSort(head)
print_linked_list(head) # head -> 1
head = array_to_linked_list([2, 1])
insertionSort(head)
print_linked_list(head) # head -> 1 -> 2
head = array_to_linked_list([1, 2, 3, 4, 5])
insertionSort(head)
print_linked_list(head) # head -> 1 -> 2 -> 3 -> 4 -> 5
head = array_to_linked_list([1, 2, 5, 8, 10, 3, 4, 6, 7, 9])
insertionSort(head)
print_linked_list(head) # head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
head = array_to_linked_list([-1,5,3,4,0]) # negative numbers
insertionSort(head)
print_linked_list(head) # head -> -1 -> 0 -> 3 -> 4 -> 5
head = array_to_linked_list([]) # empty array
insertionSort(head)
print_linked_list(head) # head ->
head = array_to_linked_list([2,2,3,4,4,4,4,3,1]) # duplicates in array
insertionSort(head)
print_linked_list(head) # head -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4
head = array_to_linked_list([-100, 20, -10, 60, 80])
insertionSort(head)
print_linked_list(head) # head -> -100 -> -10 -> 20 -> 60 -> 80
head = array_to_linked_list([10,9,8,7,6,5,4,3,2,1])
insertionSort(head)
print_linked_list(head) # head -> -100 -> -10 -> 20 -> 60 -> 80
print("----------------------------------")

