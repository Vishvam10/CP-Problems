class Solution:
    # ALTERNATE : (Literally bijection)
    #   Use 2 maps - one for map b/w pattern and s, the other
    #   for a map b/w s and pattern

    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        pattern_counter = Counter(pattern)
        words_counter = Counter(words)
        pair_counter = Counter(zip(pattern, words))

        return (len(pattern_counter) == len(words_counter) == len(pair_counter)) and (
            len(pattern) == len(words)
        )
