class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        print len(grid)
        print len(grid[0])
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                max1=grid[i][j]
                max2=grid[i][j]
                for z in range (len(grid)):
                    if grid[z][j]>max2:
                        max2=grid[z][j]
                for x in range (len(grid[0])):
                    if grid[i][x]>max1:
                        max1=grid[i][x]
                if(max1>max2):
                    max3=max2
                else:
                    max3=max1
                count=count+max3-grid[i][j]
        return count