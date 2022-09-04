
# LC206. Reverse Linked List, top100
def reverseList(self, head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr is not None:
        curr.next, prev, curr = prev, curr, curr.next
    return prev

# LC92. Reverse Linked List II - reverse between 2 nodes
def reverseBetween(self, head, m, n):
    dummy = start = ListNode(0, head)
    for _ in range(m-1): start = start.next  # move the  position before m
    pre, curr = None, start.next  # point to pre, right before cur
    for _ in range(n-m+1):  # reverse the defined part
        curr.next, pre, curr = pre, curr, curr.next
    start.next.next = curr  # point old start to tail: curr = n+1
    start.next = pre  # point start to new head
    return dummy.next

# LC24. Swap Nodes in Pairs - reverse pair
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = dummy = ListNode(None, head)
    while head and head.next:
        prev.next, head.next = head.next, head.next.next
        prev.next.next = head
        prev, head = head, head.next
    return dummy.next

# LC25. Reverse Nodes in k-Group
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    n, curr = 0, head  # find size
    while curr:
        n += 1
        curr = curr.next
    dummy = nhead = ListNode()  # the new list to insert to, nhead is previous
    ntail = None  # store temp head for next
    for _ in range(n//k):
        ntail = head  # the save the position for later jumping to
        for _ in range(k):
            head.next, nhead.next, head = nhead.next, head, head.next  # insert at nhead
        nhead = ntail  # move insertion point to the right by k steps
    ntail.next = head  # for last remainder connection
    return dummy.next

# LC2130. Maximum Twin Sum of a Linked List
def pairSum(self, head: Optional[ListNode]) -> int:
    fast, rev = head, None # use head as slow
    while fast and fast.next:  # 1, 2, 3, 2, 1    1, 2, 3, 4, 2, 1
        fast = fast.next.next
        rev, rev.next, head = head, rev, head.next
    # head = 3 2 1, tail = 2 1   head = 3 2 1, tail = 4 2 1
    tail = head.next if fast else head  # fast none when list is even
    res = 0
    while rev:
        res = max(res, rev.val + tail.val)
        head, head.next, rev = rev, head, rev.next  # restore head to original
        tail = tail.next  # 2, 3, 2, 1, then 1, 2,3,2,1
    return res

# LC234. Palindrome Linked List
def isPalindrome(self, head):
    fast, rev = head, None # use head as slow
    while fast and fast.next:  # 1, 2, 3, 2, 1    1, 2, 3, 4, 2, 1
        fast = fast.next.next
        rev, rev.next, head = head, rev, head.next
    # head = 3 2 1, tail = 2 1   head = 3 2 1, tail = 4 2 1
    tail = head.next if fast else head  # fast none when list is even
    isPali = True
    while rev:
        isPali = isPali and rev.val == tail.val
        head, head.next, rev = rev, head, rev.next  # restore head to original
        tail = tail.next  # 2, 3, 2, 1, then 1, 2,3,2,1
    return isPali

# LC143. Reorder List - odd + <even reverse>
def reorderList(self, head: ListNode) -> None:
    if not head: return
    slow = fast = head  # in 1->2->3->4->5->6 find 4
    while fast and fast.next:  # slow is the middle node
        slow, fast = slow.next, fast.next.next
    prev, curr = None, slow  # reverse the second half, prev is new head
    while curr:  # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        curr.next, prev, curr = prev, curr, curr.next
    first, second = head, prev  # merge two sorted linked lists
    while second.next:  # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first.next, first = second, first.next
        second.next, second = first, second.next
