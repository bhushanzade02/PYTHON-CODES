def letter_combinations(digits):
    if not digits:
        return []  # if empty input

    # Mapping of digits to letters
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    # Helper function for recursion
    def backtrack(index, current):
        # if we formed a full combination  __ > save it
        if index == len(digits):
            result.append(current)
            return

        # get possible letters for current digit
        for letter in mapping[digits[index]]:
            backtrack(index + 1, current + letter)

    # start recursion
    backtrack(0, "")
    return result


# --- Main program ---
digits = input("Enter digits (2-9): ")
combinations = letter_combinations(digits)

print("All possible letter combinations:")
print(combinations)
