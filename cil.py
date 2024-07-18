def find(s, start, target_char, open_bracket, close_bracket):
    # Initialize bracket count
    bracket_count = 0
    # Start searching from the given index
    for i in range(start, len(s)):
        if s[i] == open_bracket:
            bracket_count += 1
        elif s[i] == close_bracket:
            bracket_count -= 1
        elif s[i] == target_char and bracket_count == 0:
            return i
    return -1  # Return -1 if not found

# Example string and constants
s = "a[b{c}d]e"
i = 0
LBRACK = '['
RBRACK = ']'

# Call the find function
index = find(s, i, RBRACK, LBRACK, RBRACK)
print(index)  # Output should be the index of the first unmatched RBRACK from the start position
