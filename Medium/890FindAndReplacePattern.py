class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result=[]
        for word in words:
            if len(word)==len(pattern):
                patt_word= {}
                word_patt= {}
                flag=0
                for i in range (len(word)):
                    if pattern[i] in patt_word and word[i] in word[i] in word_patt:
                        if patt_word[pattern[i]]!=word[i] or word_patt[word[i]]!=pattern[i] :
                            flag=1
                    elif pattern[i] in patt_word or word[i] in word[i] in word_patt:
                        flag=1
                    else:
                        patt_word[pattern[i]]=word[i]
                        word_patt[word[i]]=pattern[i]
                        
                if flag==0:
                    result.append(word)
                    
        return result
                    
                    
        
                    
                    
                
            
                
        