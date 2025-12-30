def is_palindrome(s):
    return s == s[::-1]   # reverse and check

def palindrome_pairs(words):
    pairs = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                combined = words[i] + words[j]
                if is_palindrome(combined):
                    pairs.append([i, j])
    return pairs

# --- Main Program ---
n = int(input("Enter number of words: "))
words = []
for i in range(n):
    w = input(f"Enter word {i+1}: ")
    words.append(w)

result = palindrome_pairs(words)

print("Palindrome pairs (i, j):")
print(result)
