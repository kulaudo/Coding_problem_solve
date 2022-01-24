import unittest


def oneEdited(A, B):
  
  def solution1(A,B):
    def isDelete(A:str,B:str) -> bool:
      i,j = 0,0
      while i < len(A) and j < len(B):
        if A[i] != B[j]:
          if i != j:
            return False
          j+=1
        i += 1
        j += 1
      return True

    def isModifiedorSame(A:str, B:str) -> bool:
      return sum([1 if a != b else 0 for a, b in zip(A,B)]) <= 1
    
    if len(A) > len(B):
      A, B = B, A
    lenA, lenB = len(A), len(B)
    if lenA + 1 == lenB:
      return isDelete(A,B)
    elif lenA - lenB == 0:
      return isModifiedorSame(A,B)
    else:
      return False
  
  
  def solution2(A,B):
    
    if len(A) > len(B):
      A, B = B, A
    if len(A) < len(B)-1:
      return False

    isReplaced = False
    i,j = 0,0
    while i < len(A) and j < len(B):
      if A[i] != B[j]:
        if len(A)==len(B):
          if isReplaced:
            return False
          isReplaced = True
        else:
          if i != j:
            return False
          j+=1
      i += 1
      j += 1
    return True

  return solution2(A,B)

  
class Test(unittest.TestCase):
  def test1(self):
    self.assertTrue(oneEdited('ABC','ABC'))
  
  def test2(self):
    self.assertTrue(oneEdited('ABC','AB'))
    self.assertTrue(oneEdited('ABC','AC'))
    self.assertTrue(oneEdited('ABC','BC'))
  
  def test3(self):
    self.assertTrue(oneEdited('ABC','ABD'))
    self.assertTrue(oneEdited('ABC','AEC'))
    self.assertTrue(oneEdited('ABC','FBC'))

  def test4(self):
    self.assertTrue(oneEdited('ABC','ABCD'))
    self.assertTrue(oneEdited('ABC','AFBC'))
    self.assertTrue(oneEdited('ABC','GABC'))

  def test5(self):
    self.assertFalse(oneEdited('aaa','cca'))
    self.assertFalse(oneEdited('aaa','cac'))
    self.assertFalse(oneEdited('aaa','acc'))

  def test6(self):
    self.assertFalse(oneEdited('aaa','a'))
    self.assertFalse(oneEdited('abc','aaabc'))

if __name__ == '__main__':
  unittest.main()
