import unittest


def solution(String):
  def hash_table(String):
    # T: O(N) S:O(N)
    from collections import Counter
    k_has_1 = None

    for k,v in Counter(String).items():
      if v % 2 == 1:        
        if k_has_1 is None:
          k_has_1 = k
        elif k != k_has_1:
          return False
          
    return True
  
  def bitwize(String):
    # T:O(N) S:O(1)
    x = 0
    for i in range(len(String)):
      x ^= ord(String[i])
    if len(String) % 2==0:
      return x == 0
    else:
      return chr(x) in String


  if not String:
    return False

  String = String.replace(' ','').lower()
  return hash_table(String)


class Test(unittest.TestCase):
  
  def test1(self):
    self.assertTrue(solution('Tact Coa'))
  
  def test2(self):
    self.assertFalse(solution('Aba abb'))

  def test3(self):
    self.assertFalse(solution(''))

  def test4(self):
    self.assertTrue(solution('ababa'))

if __name__ == '__main__':
  unittest.main()
