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