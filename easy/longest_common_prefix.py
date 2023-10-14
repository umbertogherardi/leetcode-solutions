class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_str_len = len(strs[0])

        for str in strs:
            if len(str) < min_str_len:
                min_str_len = len(str)

        index = 0
        prefix = ""
        current_char = ""

        while index < min_str_len:
            current_char = strs[0][index]
            for str in strs:
                if (str[index] != current_char):
                    return prefix
            prefix += current_char
            index += 1

        return prefix
