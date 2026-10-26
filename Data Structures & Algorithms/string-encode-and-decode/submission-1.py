class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, encodedStr: str) -> List[str]:
        decodedStr = []
        i = 0

        while i < len(encodedStr):
            j = encodedStr.index("#", i)
            length = int(encodedStr[i:j])
            i = j + 1

            decodedStr.append(encodedStr[i:i + length])
            i += length

        return decodedStr