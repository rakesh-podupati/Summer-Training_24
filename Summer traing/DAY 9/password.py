class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # Caps: 65 to 90
        # Small: 97 to 122
        # Digits: 48 to 57
        special_char = "!@#$%^&*()-+"
        lower = 0
        upper = 0
        digit = 0
        special = 0
        adjacent = 0
        if len(password) >= 8:
            for i in password:
                if i in special:
                    special += 1
                else:
                    i = ord(i)
                    if (i >= 65 and i <= 90):
                        lower += 1
                    elif (i >= 97 and i <= 122):
                        upper += 1
                    elif (i >= 48 and i <= 57):
                        digit += 1

        return false