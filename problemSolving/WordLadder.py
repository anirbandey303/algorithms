####we will need string library
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        present = False
        myBag = set()
        for word in wordList:
            if(endWord == word):
                present = True
            myBag.add(word)
        if(present == False):
            return 0
        
        queue = list()
        queue.append(beginWord)
        depth = 0
        while(queue):
            depth += 1
            lCount = len(queue)
            while(lCount != 0):
                word = queue.pop(0)
                for i in range(len(word)):
                    for j in string.ascii_lowercase:
                        temp = word
                        temp = list(temp)
                        temp[i] = j
                        temp = ''.join(temp)
                        if(temp == word):
                            continue
                        if(temp == endWord):
                            return depth+1
                        if(temp in myBag):
                            queue.append(temp)
                            myBag.remove(temp)
                            #print(queue)
                lCount -= 1
        return 0


#################################################################################################
#v0.2

import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        mySet = set()
        for word in wordList:
            mySet.add(word)
        if(endWord not in mySet):
            return 0
        #alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        queue = list()
        depth = 0
        queue.append(beginWord)
        
        while(queue):
            depth += 1
            levelCount = len(queue)
            while(levelCount > 0):
                word = queue.pop(0)
                for i in range(len(word)):
                    for j in string.ascii_lowercase:
                        temp = list(word)
                        temp[i] = j
                        temp = ''.join(temp)
                        if(temp == word):
                            continue
                        if(temp == endWord):
                            return depth + 1
                        if(temp in mySet):
                            queue.append(temp)
                            mySet.remove(temp)
                levelCount -= 1
        return 0