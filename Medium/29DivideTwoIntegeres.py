class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        count=1
        absdd=abs(dividend)
        absdv=abs(divisor)
        exponential=absdv
        exponentialcount=1
        
        if divisor==dividend:
            return 1
        while(absdv<=absdd):
            
            
                
            absdv=absdv+exponential
            count=count+exponentialcount
            print "entry",absdv,count,exponentialcount,exponential
            exponential=exponential+exponential
            exponentialcount=exponentialcount+exponentialcount
            if(exponential+exponential>absdd):
                print "breaking point"
                exponential=abs(divisor)
                exponentialcount=1
            if(absdv+exponential>=absdd):
                print "breaking point"
                exponential=abs(divisor)
                exponentialcount=1
        print "exit",absdv,count,exponentialcount,exponential
            
        count=count-exponentialcount
        
        if count>2147483647 and ((divisor<0 and dividend<0) or (divisor > 0 and dividend >0)):
            count=2147483647
        if count>=2147483647 and ((divisor<0 and dividend>0) or (divisor > 0 and dividend <0)):
            count=2147483648       
        if divisor<0 and dividend<0:
            print "positive"
            return count
        elif (divisor > 0 and dividend <0) or (divisor < 0 and dividend >0):
            print "negative"
            return (count-(count+count))
        
        return count
            
            
            