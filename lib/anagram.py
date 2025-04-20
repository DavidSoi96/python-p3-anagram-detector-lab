# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, is_anagrams):
        matches = []
        for the_word in is_anagrams:
            the_word_lower = the_word.lower()
            if the_word_lower != self.word  and sorted(the_word_lower) == self.sorted_word:
                matches.append(the_word)
        return matches 