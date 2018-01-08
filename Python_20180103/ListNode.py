class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, pre, cur, newNode):
        pre.next = newNode
        newNode.next = cur

    def delete(self, pre, cur):
        pre.next = cur.next

    def traverse(self, head):
        while head:
            print(head.val)
            head = head.next
