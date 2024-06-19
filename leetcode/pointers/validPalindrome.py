class Solution:
    def isPalindrome(self, s):
        alphaString=''.join([char for char in s if char.isalnum()]).lower()

        length=len(alphaString)
        for i in range(0,length//2):
            if alphaString[i]!=alphaString[length-1-i]:
                return False
        return True