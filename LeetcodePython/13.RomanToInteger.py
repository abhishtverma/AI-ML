class Solution(object):
    def romanToInt(self, s):
        values={
        "I": 1, "V": 5, "X": 10, "L": 50, "C":100,       
        "D":  500, "M": 1000 
        }
        total = 0

        for i in range (len(s)-1):
            if values [s[i]]<values [s[i+1]]:
                total=total-values [s[i]]
            else:
                total=total+values[s[i]]
        total=total+values[s[-1]] 
        # S[-1] for last digit addition we can also write values[s[len(s) - 1]] both are same
        return total   