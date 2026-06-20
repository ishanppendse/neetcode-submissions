# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.prev = None

def step_fwd(node):
    if node.next is not None:
        node.next.prev = node
    return node.next, node

def step_back(node):
    return node.prev, node

def remove_node(node):
    if node.next is None:
        if node.prev is None:
            # singular node
            return None
        node.prev.next = None
        # node is last in LL
        return node.prev
    node.next.prev = node.prev
    if node.prev is not None:
        node.prev.next = node.next
    # all other cases
    return node.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while count<30:
            count += 1
            cur, prev = step_fwd(cur)
            if cur is None:
                cur = prev
                break
        count = 0
        while count<30:
            count += 1
            if count == n:
                cur = remove_node(cur)
                if cur is None:
                    return None
            cur, next = step_back(cur)
            if cur is None:
                return next
            
        
