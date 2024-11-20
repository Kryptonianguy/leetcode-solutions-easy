'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

    @staticmethod
    def createLinkedList(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    @staticmethod
    def linkedListToList(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

sol = Solution()

head = Solution.createLinkedList([1, 1, 2])
new_head = sol.deleteDuplicates(head)
print(Solution.linkedListToList(new_head))

head = Solution.createLinkedList([1, 1, 2, 3, 3])
new_head = sol.deleteDuplicates(head)
print(Solution.linkedListToList(new_head))