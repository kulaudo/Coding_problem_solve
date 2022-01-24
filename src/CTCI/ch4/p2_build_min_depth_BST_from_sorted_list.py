from unittest import TestCase, main
import unittest
from data_structure.data_structure import TreeNode

def solution(unique_nums:list[int]) -> TreeNode:
  if not unique_nums:
    return
  mid = len(unique_nums) // 2
  left = solution(unique_nums[:mid])
  right = solution(unique_nums[mid+1:]) 
  return TreeNode(unique_nums[mid], left, right)

def sameTree(root1:TreeNode, root2:TreeNode) -> bool:
  if not root1 and not root2:
    return True
  if not root1 or not root2:
    return False
  return root1.val == root2.val and sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)

class Test(TestCase):
  def test1(self):
    data = [1,3,4,5,6,8,9]
    expectResult = TreeNode(5,TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(6), TreeNode(9)))
    actual = solution(data)
    self.assertTrue(sameTree(actual, expectResult),f'expect:{expectResult}, actual:{actual}')
    
  def test2(self):
    data = []
    expectResult = None
    actual = solution(data)
    self.assertTrue(sameTree(actual, expectResult),f'expect:{expectResult}, actual:{actual}')

if __name__ == '__main__':
  unittest.main()