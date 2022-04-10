def split_in_half (s):
    length = len(s)
    half = length//2
    add = 0
    if length % 2:
        add = 1

    left = s[:half + add]
    right = s[half + add:]
    return right + left
str_test_odd = 'aaabccc'
str_test_even = 'aaabbb'
print(str_test_odd)
print(split_in_half(str_test_odd))
print(str_test_even)
print(split_in_half(str_test_even))