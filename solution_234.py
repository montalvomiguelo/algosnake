def isPalindrome(head):
    slow = head
    fast = head

    # find second half
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    curr = slow
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # traverse second half and compare
    dummy = head
    while prev:
        if prev.val != dummy.val:
            return False
        prev = prev.next
        dummy = dummy.next

    return True
