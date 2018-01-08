# Delete LinkList

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

from Python_20180103.ListNode import ListNode


class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """

    def __init__(self):
        arraylist = [1, 2, 3, 3, 4, 5, 8, 3, 5, 3, 2, 4]
        self.nodes = ListNode(-1)
        currentNode = self.nodes
        count = 0
        for val in arraylist:
            if count == 0 :
                self.nodes.val = val
                count = count +1;
                continue;
            newnode = ListNode(val)
            currentNode.next = newnode
            currentNode =  currentNode.next
        print(self.nodes)

    def removeElements(self, val):
        # write your code here
        head = self.nodes
        vals = head.traverse(head)
        if vals == val:
            head.delete()

