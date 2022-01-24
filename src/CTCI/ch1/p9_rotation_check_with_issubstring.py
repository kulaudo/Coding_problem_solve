import unittest

def rotation_check_with_issubstring(string: str, rotatedString: str) -> bool:

  return string in rotatedString*2
  


class Test(unittest.TestCase):
  ### valid cases  ###

  def test1(self):
    s1 = 'abcde'
    s2 = 'cdeab'
    self.assertTrue(rotation_check_with_issubstring(s1,s2))


  def test2(self):
    s1 = '11'
    s2 = '11'
    self.assertTrue(rotation_check_with_issubstring(s1,s2))


  ### Fail cases ###
  def test3(self):
    s1 = ''
    s2 = ''
    self.assertTrue(rotation_check_with_issubstring(s1,s2))


  ### Invalid Cases ###
  def test4(self):
    with self.assertRaises(TypeError): 
      rotation_check_with_issubstring(1,2)


if __name__=='__main__':
  unittest.main()
