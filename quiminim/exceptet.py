import re

# Example pattern to match three groups of uppercase letters
acronym3_re = re.compile(r'([A-Z])([A-Z])([A-Z])')

# Example name
name = "ABC DEF GHI"

# Perform substitution
name = acronym3_re.sub(r'\1\2\3', name)

print(name)  # Output will be: "ABC DEF GHI"
