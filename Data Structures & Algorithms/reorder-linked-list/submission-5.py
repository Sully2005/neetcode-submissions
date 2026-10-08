# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: 
            return
        nodes = []
        current = head
        while current: 
            nodes.append(current)
            current = current.next
        left_i, right_i = 0, len(nodes) - 1
        while left_i < right_i:
            nodes[left_i].next = nodes[right_i]
            left_i += 1 
            if left_i >= right_i: 
                break
            nodes[right_i].next = nodes[left_i]
            right_i -= 1

        nodes[left_i].next = None