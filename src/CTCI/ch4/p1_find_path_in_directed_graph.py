from typing import List
from collections import defaultdict, deque
import unittest
"""Find if there exists a path between two nodes in a directed graph"""

# BFS from both end: T O(2*(K)^(d/2)) for k nodes and depth d
def solution(graph:List[List[str]], v1:str, v2:str) -> bool:

  adj_list = defaultdict(list)
  process = set()
  seen = set()
  seen.add(v1)
  seen.add(v2)
  for vertex1, vertex2 in graph:
    adj_list[vertex1].append(vertex2)
    adj_list[vertex2].append(vertex1)
  
  queue = deque([(v1,v1),(v2,v2)])
  while queue:
    for _ in range(len(queue)):
      node, root = queue.popleft()
      process.add(node)
      if node in process[v1] and node in process[v2]:
        return True
      for child in adj_list[node]:
        if child not in seen:
          seen.add(child)
          queue.append((child, root))
  return False

class Test(unittest.TestCase):
  

  def test1(self):
    graph = [['a','b'],['b','d'],['d','e']]   
    self.assertTrue(solution(graph,'a','b'))

  def test2(self):
    graph = [['a','b'],['b','d'],['d','e'],['f','g']]
    self.assertFalse(solution(graph,'a','f'))
    


if __name__ == '__main__':
    unittest.main()
