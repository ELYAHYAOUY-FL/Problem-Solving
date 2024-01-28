class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
       if len(text1)==0 or len(text2)==0 :
           return 0 
       elif (len(text1)==1) and  (text1 in text2) :
           return 1 
       elif text1[0]==text2[0]:
          return 1 + self.longestCommonSubsequence(text1[1:],text2[1:])
           
       else :
           return max(self.longestCommonSubsequence(text1,text2[1:]) , self.longestCommonSubsequence(text1[1:],text2))
                                
    
solution1 = Solution()
text1 = "kjhxybyrgzczy"
text2= "hafcdqbgncrcbihkd"
num = solution1.longestCommonSubsequence(text1, text2)

print(num)