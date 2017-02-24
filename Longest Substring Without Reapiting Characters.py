# reference
# Google 
# Reputation:  459

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        because every substring can only have ONE char apprear once, we can
        record this char's place
        """
        if s == "":
            return 0
        charUsed = {}
        maxLength = 0
        startplace = 0
        for i in range(len(s)):
            if s[i] in charUsed :
                startplace = max(charUsed[s[i]] + 1 ,startplace)
                # print("find "+s[i]+"and start at %d"%startplace)
            maxLength = max(maxLength, i - startplace)
            charUsed[s[i]] = i
                    
        return maxLength+1
                