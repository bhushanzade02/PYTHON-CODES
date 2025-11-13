def min_window_subsequence(s1, s2):
    n, m = len(s1), len(s2)
    min_len = float('inf')
    start = -1

    i = 0
    while i < n:
        j = 0
        # Step 1: move forward to find a full match of s2 in s1
        while i < n:
            if s1[i] == s2[j]:
                j += 1
                if j == m:
                    break
            i += 1

        # no full match found  break
        if j < m:
            break

        # Step 2: move backward to find smallest possible window
        end = i
        j -= 1
        while j >= 0:
            if s1[i] == s2[j]:
                j -= 1
            i -= 1

        i += 1  # move to start of the valid window
        window_len = end - i + 1

        if window_len < min_len:
            min_len = window_len
            start = i

        # Step 3: continue search after this starting point
        i = i + 1

    # Step 4: return result
    if start == -1:
        return ""
    return s1[start:start + min_len]


# Example
s1 = input("Enter string s1: ")
s2 = input("Enter string s2: ")

result = min_window_subsequence(s1, s2)
if result:
    print("Minimum window substring:", result)
else:
    print("No valid substring found.")
