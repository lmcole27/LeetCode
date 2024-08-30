class Solution(object):
  def islandPerimeter(self, grid):
      """
      :type grid: List[List[int]]
      :rtype: int
      """
      length = len(grid)
      width = len(grid[0])
      perimeter = 0

      for l in range(length):
        for w in range(width):
          if grid[l][w] == 1:
            perimeter += 4  
            if l > 0 and grid[l][w] == 1 and grid[l-1][w] == 1:
              perimeter -= 2
            if w > 0 and grid[l][w] == 1 and grid[l][w-1] == 1:
              perimeter -= 2
      return perimeter

s = Solution()
print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))