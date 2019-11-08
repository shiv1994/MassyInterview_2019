class MissingLetters:
    def getMissingLetters(self, sentence):
        letter_exists = [False for i in range(0,26)]
        missing_letters = []
        sentence = sentence.lower()
        for i in range(0, len(sentence)):
            ch = sentence[i]
            loc = (ord(ch) - ord('a'))
            letter_exists[loc] = True
        for i in range(0, 26):
            if not letter_exists[i]:
                missing_letters.append(chr(ord('a') + i))
        return missing_letters

msl = MissingLetters()
print(msl.getMissingLetters('abcz'))