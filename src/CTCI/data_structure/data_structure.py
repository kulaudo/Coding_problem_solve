class Node:
  val = None
  children = None

  def __init__(self, val=None, children=[]) -> None:
    self.val = val
    self.children = children

class TreeNode:
  def __init__(self, val=None, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

