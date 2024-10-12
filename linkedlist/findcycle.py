# Leetcode question number: 141 https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False