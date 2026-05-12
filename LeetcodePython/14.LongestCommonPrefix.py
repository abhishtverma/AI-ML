class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        first = strs[0]

        for i in range (len(first)):
         for j in strs[1:]:#[1:]means from 1st position to last not 0th position
           if i >= len(j) or j[i]!= first[i]:
              return first[:i] #[:i]means upto/before the number not this 
        return first   
