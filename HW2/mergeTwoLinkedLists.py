# pylint: skip-file
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeTwoLinkedLists(A, B):
    if not A.next:
        return B
    
    if not B.next:
        return A

    real_A = A.next
    real_B = B.next
    dummy = Node("head")
    node=dummy
    while real_A and real_B:
        if real_A.val > real_B.val :
            node.next=real_B
            real_B=real_B.next
        else:
            node.next=real_A
            real_A=real_A.next
        node=node.next
    
    while real_A:
        node.next =real_A
        real_A=real_A.next
        node=node.next
    
    while real_B:
        node.next=real_B
        real_B=real_B.next
        node=node.next

    return dummy
    
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


print('--------------Test mergeTwoLinkedLists--------------')
A = array_to_linked_list([2, 4, 5, 7])
B = array_to_linked_list([1, 2, 3, 6])
print_linked_list(mergeTwoLinkedLists(A, B))
# head -> 1 -> 2 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
A = array_to_linked_list([1, 3, 5, 7])
B = array_to_linked_list([])
print_linked_list(mergeTwoLinkedLists(A, B))
# head -> 1 -> 3 -> 5 -> 7
A = array_to_linked_list([])
B = array_to_linked_list([2, 4, 6, 8])
print_linked_list(mergeTwoLinkedLists(A, B))
# head -> 2 -> 4 -> 6 -> 8
A = array_to_linked_list([2])
B = array_to_linked_list([2, 4, 6, 8])
print_linked_list(mergeTwoLinkedLists(A, B))
# head -> 2 -> 2 -> 4 -> 6 -> 8

# more test cases
# A and B are both empty: return nothing
A = array_to_linked_list([])
B = array_to_linked_list([])
print_linked_list(mergeTwoLinkedLists(A, B))

# B is empty: head -> 2 -> 4 -> 6 -> 8
A = array_to_linked_list([2, 4, 6, 8])
B = array_to_linked_list([])
print_linked_list(mergeTwoLinkedLists(A, B))

# only contain 1 same element : head -> 1 -> 1
A = array_to_linked_list([1])
B = array_to_linked_list([1])
print_linked_list(mergeTwoLinkedLists(A, B))

# negative numbers: head -> -8 -> -4 -> -3 -> -1 -> 0 -> 1 -> 2 -> 5
A = array_to_linked_list([-8, -4, -1, 0, 2])
B = array_to_linked_list([-3, 1, 5])
print_linked_list(mergeTwoLinkedLists(A, B))

# decimal numbers: head -> -3.7 -> -3 -> 1 -> 5 -> 9.0
A = array_to_linked_list([-3.7, 5, 9.0])
B = array_to_linked_list([-3, 1])
print_linked_list(mergeTwoLinkedLists(A, B))
print('-----------------------------------------------------')