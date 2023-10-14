# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        start_node = ListNode()
        next_node1 = ListNode()
        next_node2 = ListNode()

        if list1 == None:
            if list2 == None:
                return None
            else: 
                return list2
        else:
            if list2 == None:
                return list1

        if list1.val < list2.val:
            start_node = list1
            next_node1 = list1.next
            next_node2 = list2
        else:
            start_node = list2
            next_node1 = list1
            next_node2 = list2.next
        
        curr_node = start_node

        while True:
            if next_node1 == None:
                curr_node.next = next_node2
                return start_node
            elif next_node2 == None:
                curr_node.next = next_node1
                return start_node
            
            if next_node1.val < next_node2.val:
                curr_node.next = next_node1
                next_node1 = next_node1.next
            else:
                curr_node.next = next_node2
                next_node2 = next_node2.next
            curr_node = curr_node.next
