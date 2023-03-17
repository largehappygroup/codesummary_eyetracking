import difflib

large_string = 'the quick brown fox jumps over the lazy dog'

# A string to compare to the large string
string_to_compare = 'thee quick brown fax jump'

# Get the closest matches
closest_matches = difflib.get_close_matches(
    string_to_compare, [large_string], n=1)

# Print the closest match
print(closest_matches[0])
