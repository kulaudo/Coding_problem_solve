import unittest


def solution(String):

  def use_lib(String):
    return r'%20'.join(String.split(' '))
  
  def two_pointer(String):
    space_count = 0
    for c in String:
      if c == ' ':
        space_count += 1
    res = [None] * (len(String) + space_count*2)
    res_i, str_i = 0, 0
    while str_i < len(String):
      if String[str_i] == ' ':
        res[res_i:res_i+3] = '%20'
        res_i+=2
      else:
        res[res_i] = String[str_i]  
      res_i+=1
      str_i+=1

    return ''.join(res)

  return two_pointer(String)


class Test(unittest.TestCase):
  
  def test1(self):
    self.assertEqual(solution('John Smith'), r'John%20Smith')
  
  def test2(self):
    self.assertEqual(solution('   b '),r'%20%20%20b%20')

  def test3(self):
    self.assertEqual(solution(''), '')

  def test4(self):
    self.assertEqual(solution('aab'),'aab')

if __name__ == '__main__':
    unittest.main()