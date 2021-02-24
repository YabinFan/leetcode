from collections import defaultdict
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # initialize the dict value as empty set
        self.d = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.d[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        word_len = len(word)
        for w in self.d[word_len]:
            i = 0
            while i < word_len and (w[i] == word[i] or word[i] == '.'):
                i+=1
            if i == word_len:
                return True
        return False