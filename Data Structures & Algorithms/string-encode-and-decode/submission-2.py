class Solution:

    # Encoding function: encodes a list of strings to a single string
    def encode(self, strs: List[str]) -> str:
        res = ""

        # Append each string with its length and a delimiter (#)
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    # Decoding function: decodes a single string back to a list of strings
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # Iterate through the encoded string
        while i < len(s):
            # Find the position of the next "#"
            j = i
            while s[j] != "#":
                j += 1

            # Extract the length of the next string
            length = int(s[i:j])
            
            # Extract the actual string based on the length
            res.append(s[j + 1: j + 1 + length])

            # Move the index to the end of the current string
            i = j + 1 + length

        return res
