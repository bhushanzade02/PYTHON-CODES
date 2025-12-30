def findSubstring(s, words):

    if not s or not words:
        return []

    word_len = len(words[0])
    total_len = word_len * len(words)
    result = []

    # Count frequency of each word
    word_count = {}
    for w in words:
        word_count[w] = word_count.get(w, 0) + 1

    # Sliding window
    for i in range(len(s) - total_len + 1):
        seen = {}
        valid = True

        for j in range(0, total_len, word_len):
            part = s[i + j : i + j + word_len]

            if part not in word_count:
                valid = False
                break

            seen[part] = seen.get(part, 0) + 1
            if seen[part] > word_count[part]:
                valid = False
                break

        if valid:
            result.append(i)

    return result


# -------- INPUT PART --------
s = input("Enter the string: ")

n = int(input("Enter number of words: "))
words = []

for i in range(n):
    w = input("Enter word: ")
    words.append(w)

# -------- FUNCTION CALL --------
output = findSubstring(s, words)

print("Starting indices:", output)
