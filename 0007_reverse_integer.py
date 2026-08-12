class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        return reverse
