# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        k = len(lists)
        dic = {}
        for i in range(k):
            if lists[i] is not None:
                heappush(heap, (lists[i].val, i))
                dic[i] = lists[i]
        head = None
        prev = None
        while heap:
            _, i = heappop(heap)
            node = dic.get(i, None)
            if head is None:
                head = node
            if prev is not None:
                prev.next = node
            if node.next is not None:
                heappush(heap, (node.next.val, i))
                dic[i] = node.next
            prev = node
        return head
            