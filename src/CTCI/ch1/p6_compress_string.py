import unittest


def compress_string(A:str) -> str:

  builder = []
  i = 0
  while i < len(A):
    j = i
    while j + 1 < len(A) and A[j] == A[j+1]:
      j += 1
    builder.append(A[i]+str(j-i+1))
    i = j + 1
  res = ''.join(builder)
  return A if not len(res) < len(A) else res



class Test(unittest.TestCase):
  def test1(self):
    self.assertEqual(compress_string('aabcccccaaa'), 'a2b1c5a3')
  
  def test2(self):
    self.assertEqual(compress_string('aa'), 'aa')
  
  
  def test3(self):
    self.assertEqual(compress_string(''), '')  

if __name__ == '__main__':
  unittest.main()