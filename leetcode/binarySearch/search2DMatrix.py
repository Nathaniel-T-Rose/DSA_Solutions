def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #search row first 
        i=len(matrix)-1
        while i>=0 and target<matrix[i][0]:
            i-=1
        if i==-1:
            return False
        if matrix[i][0]==target:
            return True
        start=0
        end=len(matrix[i])-1
        while start<=end:
            j=(start+end)//2
            if matrix[i][j]>target:
                end=j-1
            elif matrix[i][j]<target:
                start=j+1
            else:
                return True
        return False
