class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for i in strs:
            res += str(len(i)) + "$" + i
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            length = ''
            while str[i] != '$':
                length += str[i]
                i += 1
            res.append(str[i + 1:int(length) + i + 1])
            i += int(length) + 1
        return res

