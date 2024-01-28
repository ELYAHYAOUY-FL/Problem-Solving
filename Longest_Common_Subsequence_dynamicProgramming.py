    #**************************optimise time ***************************************
class Solution(object):
    def __init__(self):
        self.dic = {}
    def longestCommonSubsequence(self, text1, text2):
        if (text1, text2) not in self.dic:
            if len(text1)==0 or len(text2)==0 :
                return 0  
            elif text1[0]==text2[0]:
                return 1 + self.longestCommonSubsequence(text1[1:],text2[1:]) 
                
            else :
                self.dic[(text1, text2)] = max(self.longestCommonSubsequence(text1,text2[1:]) , self.longestCommonSubsequence(text1[1:],text2))
                return  self.dic[(text1, text2)]
        else :
            return  self.dic[(text1, text2)]                       



        #*********************************optimise time && memory **************************************
class Solution(object):
    def __init__(self):
        self.dic = {}

    def longestCommonSubsequence(self, text1, text2):
        return self.lcs_helper(text1, text2, 0, 0)

    def lcs_helper(self, text1, text2, i, j):
        if (i, j) not in self.dic:
            if i == len(text1) or j == len(text2):
                self.dic[(i, j)] = 0
            elif text1[i] == text2[j]:
                self.dic[(i, j)] = 1 + self.lcs_helper(text1, text2, i + 1, j + 1)
            else:
                self.dic[(i, j)] = max(self.lcs_helper(text1, text2, i, j + 1), 
                                        self.lcs_helper(text1, text2, i + 1, j))
        return self.dic[(i, j)]


       




solution1 = Solution()
text1 = "kjhxybyrgzczy"
text2= "hafcdqbgncrcbihkd"
num = solution1.longestCommonSubsequence(text1, text2)

print(num)