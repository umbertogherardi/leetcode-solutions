class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) >= len(haystack):
            if needle == haystack:
                return 0
            else:
                return -1

        else:
            for index in range(len(haystack) - len(needle) + 1):
                if (haystack[index : index + len(needle)] == needle):
                    return index
            return -1
        