from collections import deque
from typing import Deque, List, Set

def addWord(word: str, Dict: Set):
    res: List[str] = []
    wrd = list(word)

    #Find next word in dict by changing from 'a' to 'z'
    for i in range(len(wrd)):
        s = wrd[i]
        c = 'a'
        while c <= 'z':
            wrd[i] = c
            if ''.join(wrd) in Dict:
                res.append(''.join(wrd))
            c = chr(ord(c) + 1)
        wrd[i] = s
    return res


# Method to get possible routes
def findLadders(Dicts: List[str], beginWord: str, endWord: str):

    res: List[List[str]] = []

    visit = set()

    q: Deque[List[str]] = deque()

    Dict = set()
    for i in Dicts:
        Dict.add(i)
    q.append([beginWord])

    flag = False
    while q:
        size = len(q)
        for i in range(size):

            cur = q[0]
            q.popleft()
            newadd = []

            newadd = addWord(cur[-1], Dict)

            # Add words to the path.
            for j in range(len(newadd)):
                newline = cur.copy()
                newline.append(newadd[j])

                # Found the target
                if (newadd[j] == endWord):
                    flag = True
                    res.append(newline)

                visit.add(newadd[j])
                q.append(newline)

        if (flag):
            break
            
        for it in visit:
            Dict.remove(it)
        visit.clear()
    return res


if __name__ == "__main__":
    dict = ["hot", "dot", "dog", "lot", "log"]
    firstWord = "hot"
    secondWord = "dog"

    res = findLadders(dict, firstWord, secondWord)

    for x in range(len(res)):
        print(res[x])
