class Solution:

    def encode(self, strs: List[str]) -> str:
        # convert strings to unicode equivalents
        ascii_strs = [[str(ord(ch)) for ch in s] for s in strs]
        encoded = ""
        for s in ascii_strs:
            temp = " ".join(s) + " \0 "
            encoded += temp
        return encoded
    def decode(self, s: str) -> List[str]:
        ascii_values = s.split(" ")
        word = ""
        res = []
        for ch in ascii_values:
            if ch == "\x00":
                res.append(word)
                word = ""
                continue
            if ch == "":
                continue
            word += chr(int(ch))
        return res