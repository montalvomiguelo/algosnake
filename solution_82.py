def deleteDuplicates(head):
    dummy = ListNode(0, head)
    slow = dummy
    fast = head

    while fast:
        while fast.next and (fast.val ==
                             fast.next.val):
            fast = fast.next

        if slow.next == fast:
            slow = slow.next
        else:
            slow.next = fast.next

        fast = fast.next

    return dummy.next
