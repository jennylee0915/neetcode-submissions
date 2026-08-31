class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            result = result + str(length) + "#" + s # 5#Hello5#World
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j+1
            
            length = int(s[i:j])

            start = j + 1
            end = start + length
            word = s[start:end]
            result.append(word)

            i = end
        return result
