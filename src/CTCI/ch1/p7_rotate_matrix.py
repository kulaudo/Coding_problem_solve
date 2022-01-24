import unittest


def rotate_maxtix(matrix: list[list[int]]) -> list[list[int]]:

  def changeIndex(matrix):
    start = 0
    end = len(matrix)-1
    while start < end:
      for i in range(end-start):
          matrix[start][start+i], matrix[start+i][end], matrix[end][end-i], matrix[end -
              i][start] = matrix[end-i][start], matrix[start][start+i], matrix[start+i][end], matrix[end][end-i]

      start += 1
      end -= 1

    return matrix

  def transposeAndReflect(matrix):
    N = len(matrix)    

    def transpose(matrix):
      for i in range(N):
        for j in range(i + 1,N):
          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
      
    def reflect(matrix):
      for i in range(N):
        start, end = 0, N - 1
        while start < end:
          matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
          start += 1
          end -= 1      
      
    transpose(matrix)
    reflect(matrix)
    return matrix
  
  if not matrix:
    return 
  return transposeAndReflect(matrix)


class Test(unittest.TestCase):
    def test1(self):

      matrix = [[1,2,3],[4,5,6],[7,8,9]]
      output = [[7,4,1],[8,5,2],[9,6,3]]
      self.assertEqual(rotate_maxtix(matrix), output)

    def test2(self):
      matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
      output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]      
      self.assertEqual(rotate_maxtix(matrix),output)


    def test3(self):
      self.assertEqual(rotate_maxtix([1]), [1])


if __name__ == '__main__':
  unittest.main()
