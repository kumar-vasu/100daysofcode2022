class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        lastIndex = 0
        currIndex = 0
        for i, c in enumerate(typed):
            if currIndex < len(name) and c == name[currIndex]:
                lastIndex = currIndex
                currIndex += 1
            elif c == name[lastIndex]:
                continue
            else:
                return False
        return currIndex == len(name)