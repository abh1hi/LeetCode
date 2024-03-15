#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to serve as the head of the new linked list
        current = dummy  # Pointer to traverse the result linked list
        carry = 0

        while l1 or l2 or carry:
            # Get the values or 0 if nodes are None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum with carry
            total = val1 + val2 + carry
            carry = total // 10  # Calculate the carry
            current.next = ListNode(total % 10)  # Create a new node with the digit
            current = current.next  # Move the pointer to the next node

            # Move to the next nodes in the input lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return the next node after the dummy node
