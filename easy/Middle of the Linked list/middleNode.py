# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        current = head
        while (current):
            nodes.append(current)
            current = current.next
        if (len(nodes) % 2 != 0):
            middle = nodes[round(((len(nodes)-1)/2))]
            return middle
        middle = nodes[round((len(nodes)/2))]
        return middle