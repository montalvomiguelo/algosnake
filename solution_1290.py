def getDecimal(head):
    count = 0
    dummy = head
    while dummy:
        count += 1
        dummy = dummy.next

    dummy = head
    ans = 0
    while dummy:
        count -= 1
        if dummy.val == 1:
            ans += 2 ** count
        dummy = dummy.next

    return ans
