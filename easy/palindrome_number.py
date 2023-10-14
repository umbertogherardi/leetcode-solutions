class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        reversed_string = string[::-1]
        return (string == reversed_string)
        