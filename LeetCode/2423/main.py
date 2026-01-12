class Solution:
    # Simulate the problem, the constraints are small
    def equalFrequency(self, word: str) -> bool:
        mp = Counter(word)
        for i in range(len(word)):
            ch = word[i]

            # Temporarily delete the element
            mp[ch] -= 1

            # Permanently remove if frequency is 0
            if mp[ch] == 0:
                mp.pop(ch)

            if len(set(mp.values())) == 1:
                return True

            # Add the element back
            mp[ch] += 1

        return False
