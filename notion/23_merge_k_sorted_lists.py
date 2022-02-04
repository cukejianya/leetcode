# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.build_heap(lists)
        head = prev = None
        while len(heap) > 1:
            curr = self.pop(lists)
            if not prev:
                head = prev = curr
            else:
                prev.next = curr
                prev = curr
            if curr.next:
                lists.append(curr.next)
                self.build_heap(lists) 
        return head if head else lists[0] 


    def heapify(self, arr, parent):
        k = len(arr)
        smallest = parent
        left = 2*parent + 1
        right = 2*parent + 2
        if left < k and arr[smallest].val > arr[left].val:
            smallest = left
        if right < k and arr[smallest].val > arr[right].val:
            smallest = right
        if smallest != parent:
            arr[parent], arr[smallest] = arr[smallest], arr[parent]
            self.heapify(arr, parent)
    
    def build_heap(self.arr):
        half_size = len(arr) // 2
        for idx in range(half_size, -1, -1):
            self.heapify(arr, idx)
   
    def pop(self, arr):
        arr[0], arr[-1] = arr[-1], arr[0]
        node = arr.pop()
        self.heapify(arr, 0)
        return node
