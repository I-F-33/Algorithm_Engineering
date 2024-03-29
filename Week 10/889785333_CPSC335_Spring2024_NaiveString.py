def naive_string_matcher(text, pattern):
    """This function returns the indexes where the pattern is found in the given text"""
    n = len(text)
    m = len(pattern)
    matching_indexes = []

    for s in range(n - m + 1):
        if text[s:s + m] == pattern:
            matching_indexes.append(s)

    return matching_indexes


# Taking the text as a sample
text = input("Enter the text: ")

# Taking a pattern to be searched within that sample
pattern = input("Enter the pattern: ")

matches = naive_string_matcher(text, pattern)

if matches:
    print(f"Pattern found at Positions: {matches}")
else:
    print("Pattern not found in the text.")

