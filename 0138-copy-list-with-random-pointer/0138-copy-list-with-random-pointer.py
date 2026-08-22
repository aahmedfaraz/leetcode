"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        # get all nodes
        nodes = {}
        curr = head
        while curr:
            nodes[hex(id(curr))] = curr
            curr = curr.next

        # create copies nodes
        cnodes = {}
        convert = {}
        for address in nodes:
            node = nodes[address]
            cnode = Node(node.val)
            caddress = hex(id(cnode))
            cnodes[caddress] = cnode
            convert[address] = caddress
        
        # set pointers
        for address in nodes:
            caddress = convert[address]
            node = nodes[address]
            cnode = cnodes[caddress]

            if node.next:
                nextnode = node.next
                nextnodeaddress = hex(id(nextnode))
                cnextnodeaddress = convert[nextnodeaddress]
                cnextnode = cnodes[cnextnodeaddress]
                cnode.next = cnextnode

            if node.random:
                rnode = node.random
                rnodeaddress = hex(id(rnode))
                crnodeaddress = convert[rnodeaddress]
                crnode = cnodes[crnodeaddress]
                cnode.random = crnode
        
        return cnodes[convert[hex(id(head))]]