import pytest
def searchRange(nums: list[int], target: int) -> list[int]:
  if not nums:
    return [-1,-1]
  n = len(nums)
  def bs(isleft):

    l,r = 0, len(nums)-1
    while l + 1< r:
      m = (l+r) // 2
      if isleft:
        if nums[m] < target:
          l = m
        else:
          r = m
      else:
        if nums[m] > target:
          r = m
        else:
          l = m
    if target not in [nums[l], nums[r]]:
      return -1
    if isleft:
      return l if nums[l] == target else r
    else:
      return r if nums[r] == target else l
  
  return [bs(1),bs(0)]


data = [
  ([5,7,7,8,8,10],8,[3,4]),
  ([5,7,7,8,8,10],6,[-1,-1]),
  ([],0,[-1,-1]),
  ([1],1,[0,0])
]

@pytest.mark.parametrize(('nums','target','expected'),data)
def test_search_range(nums, target, expected):
  assert searchRange(nums,target) == expected
        



if __name__ == '__main__':
  pytest.main(['','src/LeetCode'])