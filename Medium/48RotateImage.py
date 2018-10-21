class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        '''rowCount = len(matrix)
        colCount = len(matrix[0])
        tempCount=0
        for i in range (rowCount-1,-1,-1):
            for j in range (tempCount,colCount):
                #print i,j
                # temp=matrix[i][j]
                # matrix[i][j]=matrix[j][abs((rowCount-1)-i)]
                # matrix[j][abs((rowCount-1)-i)]=temp
                matrix[i][j], matrix[j][abs(rowCount-1)-i] = matrix[j][abs(rowCount-1)-i], matrix[i][j]
            tempCount=tempCount+1
        print  matrix
        print 3//2
        for i in range (0,(rowCount-1)//2):
            for j in range (i+1,(rowCount-i)-1):
                print i,j
                print j,abs((rowCount-1)-i)
                matrix[i][j], matrix[j][abs((rowCount-1)-i)] = matrix[j][abs((rowCount-1)-i)], matrix[i][j]
            
        
        print  matrix'''
        
        top=0
        bottom=len(matrix)-1
        
        while(top< bottom):
            for i in range (0,bottom-top):
                print top,bottom,i
                temp=matrix[top][top+i]
                matrix[top][top+i]=matrix[bottom-i][top]
                matrix[bottom-i][top]=matrix[bottom][bottom-i]
                matrix[bottom][bottom-i]=matrix[top+i][bottom]
                matrix[top+i][bottom]=temp
            top=top+1
            bottom=bottom-1
                
    
                
            