class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        row = [1] * n #Expand row to size of input 
        #DFS implement
        for i in range(m - 1):
            new_row = [1] * n #  Keep dimensions of new row consistent
            for j in range(n - 2, -1, -1): # for every element (minus the last row), traverse the board
                new_row[j] = new_row[j + 1] + row[j] #  populate row by adding row to the right and row to the bottom
            row = new_row 
        return row[0]

        # O(n * m) #time complexity O(n) #linear space


solution = Solution()

print(solution.uniquePaths(10,20))