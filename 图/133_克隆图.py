"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        s = {}
        if node is None:
            return None
        queue = [node]
        head = None
        while queue:
            pre = queue.pop(0)
            if pre.val in s and s[pre.val].neighbors:
                continue
            elif pre.val in s and not s[pre.val].neighbors:
                n = s[pre.val]
            else:
                n = Node()
                n.val = pre.val
            if n.val == 1:
                head = n
            for neighbors in pre.neighbors:
                queue.append(neighbors)
                if neighbors.val in s:
                    n.neighbors.append(s[neighbors.val])
                else:
                    nb = Node()
                    nb.val = neighbors.val
                    s[nb.val] = nb
                    n.neighbors.append(nb)
        return head
