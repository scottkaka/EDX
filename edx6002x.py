# import pylab
# pylab.figure(1)
# pylab.plot([1,2,3,4],[1,7,3,5])
# pylab.show()


def isAlphabeticalWord(word, wordList = None):
    if (len(word) > 0):
        curr = word[0]
    for letter in word:
        if (curr > letter):
            return False
        else:
            curr = letter
    if wordList is None:
        return True
    return word in wordList

print isAlphabeticalWord('abcd')

def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

lotsOfParameters2(b=3,3)