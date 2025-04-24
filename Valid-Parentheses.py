class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == \{\ or char == \(\ or char == \[\:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif (
                    (char == \}\ and stack[-1] == \{\)
                    or (char == \)\ and stack[-1] == \(\)
                    or (char == \]\ and stack[-1] == \[\)
                ):
                    stack.pop()
                else:
                    return False
        return not bool((stack))
