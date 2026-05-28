class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        #I want to loop through s2 with l and r, so basically a dynamic sliding window
        #As I loop through s2, I check with l. If what is at L is in s1, that's the first condition.
        #2nd condition is the count of it. I need to find a way to keep count of it.
        #what if I remove it. So if it is inside, remove from s1, my only issue now is that, if there is
        #more than one occurence in my s1 will it remove all of them or just one of them?
        from collections import Counter

        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            window[c] += 1

            if r - l + 1 > len(s1):
                left_char = s2[l]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                l += 1

            if window == need:
                return True

        return False