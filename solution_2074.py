def reverseEvenLengthGroups(head):
    i = 1
    last = None
    slow = head
    while slow:
        count = 0
        fast = slow
        prev = None
        while fast and count < i:
            prev = fast
            fast = fast.next
            count += 1

        if count % 2 != 0:
            last = prev
            slow = fast
            i += 1
            continue

        prev = None
        curr = slow
        while count:
            count -= 1
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        last.next = prev
        last = slow
        slow.next = curr
        slow = curr
        i += 1

    return head
