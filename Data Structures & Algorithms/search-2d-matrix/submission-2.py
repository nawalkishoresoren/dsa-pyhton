class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left, right = 0, (rows*columns)-1

        while(left<=right):
            mid = left + (right-left)//2

            row = mid//columns
            col = mid%columns

            if(target == matrix[row][col]):
                return True
            elif(target > matrix[row][col]):
                left = mid+1
            else:
                right = mid-1
        
        return False
        