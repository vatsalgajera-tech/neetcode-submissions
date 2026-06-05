class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        stack = []

        for ch in s:
            if ch in brackets:
                stack.append(ch)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if brackets[top] != ch:
                    return False

        return len(stack) == 0