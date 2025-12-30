def wordLadder(beginWord, endWord, wordList):

    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    graph = {}
    found = False

    level = [beginWord]   

    # -------- BFS PART --------
    while level and not found:
        next_level = []

        for word in level:
            if word in wordSet:
                wordSet.remove(word)

        for word in level:
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i+1:]

                    if new_word in wordSet:
                        if word not in graph:
                            graph[word] = []
                        graph[word].append(new_word)
                        next_level.append(new_word)

                        if new_word == endWord:
                            found = True

        level = next_level

    # -------- DFS PART --------
    result = []
    path = [beginWord]

    def dfs(word):
        if word == endWord:
            result.append(path[:])
            return

        if word not in graph:
            return

        for nxt in graph[word]:
            path.append(nxt)
            dfs(nxt)
            path.pop()

    dfs(beginWord)
    return result


# -------- INPUT --------
beginWord = input("Enter begin word: ")
endWord = input("Enter end word: ")

n = int(input("Enter number of words in dictionary: "))
wordList = []

for i in range(n):
    w = input("Enter word: ")
    wordList.append(w)

ans = wordLadder(beginWord, endWord, wordList)
print("Shortest transformation sequences:")
print(ans)
