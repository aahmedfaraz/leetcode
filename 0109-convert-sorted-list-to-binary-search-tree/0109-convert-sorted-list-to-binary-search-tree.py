# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)
            
        # 1. Find mid node
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 2. Identify left and right lists
        left = head
        right = slow.next

        # 3. Cut the list in half
        if prev:
            prev.next = None

        # 4. Create root node
        root = TreeNode(slow.val)

        # 5. Create left and right node - recursive
        leftNode = self.sortedListToBST(left)
        rightNode = self.sortedListToBST(right)

        # 6. Connect with root
        root.left = leftNode
        root.right = rightNode

        # 5. return root
        return root
        