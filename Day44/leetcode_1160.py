class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        map_chars = {}
        for i in range(len(chars)):
            if chars[i] in map_chars:
                map_chars[chars[i]] += 1
            else:
                map_chars[chars[i]] = 1

        result = 0

        for word in words:
            map_curr = copy.deepcopy(map_chars)
            dont_add = False
            for j in range(len(word)):
                if word[j] in map_curr:
                    map_curr[word[j]] -= 1
                    if map_curr[word[j]] == 0:
                        map_curr.pop(word[j])
                else:
                    dont_add = True
            if not dont_add:
                result += len(word)
            del map_curr
        return result
