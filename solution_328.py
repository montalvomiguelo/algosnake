def oddEvenList(head):
    if not head:
        return None

    dummy = head.next
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        if not fast:
            break
        slow.next.next = fast.next
        slow.next = fast
        slow = fast

    slow.next = dummy

    return head
