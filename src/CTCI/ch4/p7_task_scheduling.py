import unittest
from collections import defaultdict

def solution(jobs, dependencies):
  
  def topological_sort_bfs(jobs, dependencies):
    from collections import deque

    # build dep list, pre list
    dep_list = defaultdict(int)
    todo_list = defaultdict(list)
    for dep, job in dependencies:
      dep_list[job] += 1
      todo_list[dep].append(job)
    
    result = []

    # use queue to store jobs need to be finished first
    # finish job without dependencies
    # and then finish the job without dependencies
    # if still have unfinished job, return False

    q = deque([])
    for job in jobs:
      if job not in dep_list:
        q.append(job)
    for job, deps in dep_list.items():
      if deps == 0:
        q.append(job)
    
    while len(q) > 0:
      for _ in range(len(q)):
        done_job = q.popleft()
        result.append(done_job)

        for todo in todo_list[done_job]:
          dep_list[todo] -= 1
          if dep_list[todo] == 0:
            q.append(todo)
    return result if all([v == 0 for v in dep_list.values()]) else []
      
  return topological_sort_bfs(jobs,dependencies)



class Test(unittest.TestCase):
  
  def check_result_by_set(self, answer, predefined_set) -> bool:
    level = 0
    current = 0
    for item in answer:
      if item not in predefined_set[level]:
        return False
      current += 1
      if current == len(predefined_set[level]):
        level += 1
        current = 0
    return level == len (predefined_set)

  def test1(self):
    levels= {0: ['f','e'], 1: ['a','b'], 2:['d'], 3:['c']}
    ans = solution(['a','b','c','d','e','f'],[('a','d'),('f','b'),('b','d'),('f','a'),('d','c')])    
    check = self.check_result_by_set(ans, levels)
    self.assertTrue(check)

  def test2(self):
    ans = solution(['a','b','c','d','e','f'],[('a','d'),('d','c'),('c','a')])
    self.assertEqual(ans, [])


if __name__ == '__main__':
    unittest.main()
