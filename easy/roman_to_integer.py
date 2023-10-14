class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I": 1, 
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prev_int = roman_dict[s[0]]
        converted_int = 0
        
        for numeral in s:
            print(numeral)
            if (prev_int < roman_dict[numeral]):
                converted_int -= prev_int * 2
            converted_int += roman_dict[numeral]
            prev_int = roman_dict[numeral]

        return converted_int
