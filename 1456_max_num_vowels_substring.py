class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window_start = 0
        vowels = ['a','e','i','o','u']
        max_vow = 0
        count = 0
        for window_end in range(len(s)):
            if s[window_end] in vowels:
                count+=1
            if window_end >=k-1:
                max_vow = max(max_vow, count)
                if s[window_start] in vowels:
                    count-=1
                window_start +=1
        return max_vow
