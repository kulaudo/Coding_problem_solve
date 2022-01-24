import unittest


def is_unique_string(string):
  if not string:
    return False
  
  def bruteforce(string):
    # T: O(N^2) | S:O(1)
    for i in range(len(string)):
      for j in range(i+1, len(string)):
        if string[i]==string[j]:
          return False
    return True
  
  
  def hash_table(string):
    # T: O(N) | S:O(N)
    seen_char = set()
    for i in range(len(string)):
      if string[i] not in seen_char:
        seen_char.add(string[i])
      else:
        return False
    return True


  def bitwize(string):
    # T: O(N) | S:O(1)
    compare = ord(string[0])
    for i in range(1,len(string)):
      compare ^= ord(string[i])
      if compare == 0:
        return False
    return True
      
  return bitwize(string)


class Test(unittest.TestCase):
  
  def test1(self):
    self.assertTrue(is_unique_string('abcd'))
  
  def test2(self):
    self.assertTrue(is_unique_string('a'))

  def test3(self):
    self.assertFalse(is_unique_string(''))

  def test4(self):
    self.assertFalse(is_unique_string('aab'))

if __name__ == '__main__':
  unittest.main()
  