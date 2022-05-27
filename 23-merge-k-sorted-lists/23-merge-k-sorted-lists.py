
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        items = []
        for node in lists:
            while node != None:
                items.append(node.val)
                node = node.next
                
        items.sort()
        
        head = ListNode()
        tail = head
        
        for i in range(len(items)):
            tail.val = items[i]
            if i < len(items)-1:
                tail.next = ListNode()
            tail = tail.next
            
        if head == tail:
            return None
            
        return head
            
            
        
        
        
            
                
            
        
        