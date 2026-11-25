class Solution:
    def encode(self, strs: list[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        n = len(s)
        while i < n:
            # Read the length digits up to '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # The string starts right after '#'
            start = j + 1
            result.append(s[start:start + length])
            i = start + length
        return result