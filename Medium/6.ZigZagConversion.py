class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
            
        result_array = []
        for i in range(numRows+1):
            result_array.append([])
        current_row = 0
        i = 0
        while i < len(s):
            result_array[current_row].append(s[i])
            print i
            print "outer"
            current_row += 1
            i += 1
            if current_row == numRows:
                current_row = numRows-2
                while current_row != 0 and i < len(s):
                    print i
                    print "inner"
                    result_array[current_row].append(s[i])
                    current_row -= 1
                    i += 1
        result = ''
        for i in result_array:
            result += ''.join(i)
        return result