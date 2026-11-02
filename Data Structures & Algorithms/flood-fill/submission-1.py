#it put the given cooridnate in orig, then checks if it is equal to the color they wwant, if same return cooridnates then initialise row and col, make dfs FUNCTION and call row and column, if it is out of bounds or the pixel colour doesn't match orig then return

#else change the pixel to new colour and call DFS again on its neighbours(up, down left, right)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image

        m, n = len(image), len(image[0])

        def dfs(r, c):
            if r<0 or r>=m or c<0 or c>=n or image[r][c] != orig:
                return
            

            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image