import unittest
from collections import Counter


def solution(A,B):
  if not A or not B:
    return False
  if len(A) > len(B):
    A,B = B,A

  def hash_table(A,B):
    # T:O(A+B), S:O(A+B)
    countA = Counter(A)
    countB = Counter(B)
    for k, v in countA.items():
      if k not in countB or v > countB[k]:
        return False
    return True

  def sorting(A,B):
    # T: O(AlogA + BlogB) S:O(A+B)
    a = sorted(list(A))
    b = sorted(list(B))
    i, j = 0,0
    while i < len(a):
      if a[i]!=b[j]:
        return False
      if i + 1 < len(a) and a[i+1] != a[i]:
        while b[j+1]==b[j]:
          j += 1
      i += 1
      j += 1
    return True
      

  return sorting(A,B)

class Test(unittest.TestCase):
  
  def test1(self):
    self.assertTrue(solution('acbd','abcdefgh'))
  
  def test2(self):
    self.assertTrue(solution('ababa','aab'))

  def test3(self):
    self.assertFalse(solution('','a'))

  def test4(self):
    self.assertFalse(solution('a','bcd'))

if __name__ == '__main__':
    unittest.main()
  