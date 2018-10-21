class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        startIndex=0
        if len(str)<1:
            return 0
        sign=0
        negative=False
        for i in range (len(str)):
            if not str[i].isspace():
                
                if str[i].isdigit() or (str[i]=='-' and sign==0) or (str[i]=='+' and sign==0):
                    if str[i]=='-':
                        sign=1
                        negative=True
                        if len(str)>=i+2:
                            startIndex=i+1
                            break
                        else:
                            return 0
                    elif str[i]=='+':
                        sign=1
                        negative=False
                        if len(str)>=i+2:
                            startIndex=i+1
                            break
                        else:
                            return 0
                    else:
                        startIndex=i
                        break
                
                else:
                    return 0
        
        
        result=0
        print "Start WIth",str[startIndex]
        
        if not str[startIndex].isnumeric():
            return 0
        while (str[startIndex].isnumeric()):
            print startIndex
            result=result*10 + int(str[startIndex])
            startIndex+=1
            if startIndex==len(str):
                break
        
        if result >= 2**31 and not negative :
            result=2**31-1
        elif result > 2**31 and negative:
            result=2**31
        if negative:
            return result*-1
        else:
            return result