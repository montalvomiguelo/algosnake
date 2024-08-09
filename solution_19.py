def removeNthFromEnd(head, n):
    slow = head
    fast = head

    for _ in range(n):
        fast = fast.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    if not fast:
        head = slow.next
    else:
        slow.next = slow.next.next

    return head
