"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
  def copyRandomList(self, head: 'Node') -> 'Node':
    if not head:
      return None
    if head in self.map:
      return self.map[head]
    newNode = Node(head.val)
    self.map[head] = newNode
    newNode.next = self.copyRandomList(head.next)
    newNode.random = self.copyRandomList(head.random)
    return newNode
  map = {}        
