# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for llist in lists:
            while(llist):
                self.add_to_heap(heap, llist)
                llist = llist.next
        head = self.remove_from_heap(llist)
        curr = head
        while(len(heap)):
            curr.next = self.remove_from_heap(llist)
            curr = curr.next
        curr.next == None
        return heap

    def add_to_heap(self, heap, node):
        heap.append(node)
        idx = len(heap)
        while(idx)
            parent_idx = (idx - 1) // 2
            parent = heap[parent_idx]
            if heap[idx].val < parent.val:
                heap[parent_idx] = heap[idx]
                heap[idx] = parent
            else:
                break
            idx = parent_idx

    def remove_from_heap(self, heap):
        removing_node = heap[0]
        heap[0] = heap.pop()
        idx = 0
        while(idx * 2 < len(heap) - 1):
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2
            smaller_child_idx = 0
            if heap[left_idx].val > heap[right_idx].val:
                smaller_child_idx = right_idx 
            else:
                smaller_child_idx = left_idx
            child = heap[smaller_child_idx]
            if heap[idx].val > child.val:
                heap[smaller_child_idx] = heap[idx]
                heap[idx] = child
            else:
                break
            idx = smaller_child_idx 
        return removing_node



