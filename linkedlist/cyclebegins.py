def detectcycle(head):
    slow,fast=head,head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next
        if slow==fast:
            while head!=fast:
                head=head.next
                fast=fast.next
            return head

        return None
