class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count_right = 0
        for char in s:
            a_count_right += 1 if char == 'a' else 0

        b_count_left = 0
        res = len(s)

        for i in range(len(s)):
            if s[i] == 'a':
                a_count_right -= 1
            res = min(res, a_count_right + b_count_left)
            if s[i] == 'b':
                b_count_left += 1

        return res