#single linked list qiestions
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from linked_list.single_linked_list import *


# function to find nth element from last
def findNthfromlast(data, n) :
    length = 0 

    itr = data.head

    while itr :
        length += 1
        itr = itr.next

    itr = data.head
    for i in range (1, length-n+1) :
        itr = itr.next
    
    print(itr.data)
    return itr.data   


# function to check if loop exists in linked list
def detectLoop(head) :
    list = []

    itr = head

    while itr :
        if itr in list :
            return True
        
        list.append(itr)
        itr = itr.next

    return False    



if __name__ == '__main__' :
    ll = SingleLinkedList()
    
    ll.insert_values(["banana", "apple", "mango", "seeds"])
    
    findNthfromlast(ll, 4)

    # Create a hard-coded linked list:
    # 1 -> 3 -> 4
    head = Node(1, None)
    head.next = Node(3, None)
    head.next.next = Node(4, None)

    # Create a loop
    head.next.next.next = head.next
    
    result = detectLoop(head)
    print(result)