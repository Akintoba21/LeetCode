class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split(' ')
        sentence2 = sentence2.split(' ')
        gcsl = 0
        gcsr = 0
        l = min(len(sentence1), len(sentence2))
        for x in range(l):
            if sentence1[x] != sentence2[x]: break
            gcsl += 1
        for x in range(l):
            if sentence1[-(x+1)] != sentence2[-(x+1)]: break
            gcsr += 1
        return gcsl + gcsr >= l