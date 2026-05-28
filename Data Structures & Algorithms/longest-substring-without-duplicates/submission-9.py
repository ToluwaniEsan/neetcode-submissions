class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #length of longest substring without duplicate characters
        #substring is a contiguous sequence of characters within a string

        lenstr = 1
        maxstr = 1
        if not s:
            return 0
        else:
            substr = s[0]

        for i in range(1, len(s)):
            if s[i] not in substr:
                substr = substr + s[i]
                lenstr += 1
                maxstr = max(maxstr, lenstr)

            else:
                for j in range(len(substr)):
                    if substr[j] == s[i]:
                        substr = substr[j+1:]
                        break
                substr = substr + s[i]
                lenstr = len(substr)
                maxstr = max(maxstr, lenstr)

        return maxstr