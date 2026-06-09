class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        forward = 0
        backward = len(s) - 1

        while forward < backward:
            while forward < backward and not s[forward].isalnum():
                forward += 1

            while forward < backward and not s[backward].isalnum():
                backward -= 1

            print(s[forward].lower(), s[backward].lower())

            if s[forward].lower() != s[backward].lower():
                return False
            
            forward += 1
            backward -= 1

        return True