"""
Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
"""
word = "Put several strings within parentheses to have them joined together"

print(word[:2])  # character from the beginning to position 2 (excluded)

print(word[4:])  # characters from position 4 (included) to the end

print(word[-2:])  # characters from the second-last (included) to the end
