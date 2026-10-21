class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "\0"
        return "\n".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "\0":
            return []
        result = []
        word = []
        for i in range(0,len(s)+1):
            if i == len(s) or s[i] == "\n":
                result.append("".join(word))
                word.clear()
            else:
                word.append(s[i])
        return result

