from linkedList import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_list, right_list = split(linked_list)
    left = merge_sort(left_list)
    right = merge_sort(right_list)
    return merge(left, right)

def split(linked_list):
    """
    splits the linked list into two parts from midpoint
    """

    if linked_list == None or linked_list.head == None:
        left_list = linked_list
        right_list = None
        return left_list, right_list
    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.nodeAtIndex(mid - 1)
        left_list = linked_list
        right_list = LinkedList()
        right_list.head = mid_node.next_node
        mid_node.next_node = None
        return left_list, right_list

def merge(left, right):
    """
    merges two list by taking the Node with largest data first
    """
    merged = LinkedList()
    # fake head
    merged.insert(0,0)
    current = merged.head
    left_current = left.head
    right_current = right.head

    while left_current or right_current:
        if left_current is None:
            current.next_node = right_current
            right_current = right_current.next_node
        elif right_current is None:
            current.next_node = left_current
            left_current = left_current.next_node
        else:
            if left_current.data < right_current.data:
                current.next_node = left_current
                left_current = left_current.next_node
            else:
                current.next_node = right_current
                right_current = right_current.next_node
        current = current.next_node
    
    # discard fake head
    head = merged.head.next_node
    merged.head = head

    return merged

def verify_sort(linked_list):
    if linked_list is None or linked_list.size() == 0 or linked_list.size() == 1:
        return True
    else:
        first_node = linked_list.nodeAtIndex(0)
        second_node = linked_list.nodeAtIndex(1)
        rest_list = LinkedList()
        rest_list.head = second_node
        return first_node.data <= second_node.data and verify_sort(rest_list)

        
l = LinkedList()
l.insert(99, 0) 
l.insert(7, 0)  
l.insert(88, 0) 
l.insert(4, 4) 
l.insert(4, 3) 