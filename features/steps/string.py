def unique_char(s):
    if len(s) == 1:
        return True
    chars = set()
    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True

test_str_positive = 'abcde'
test_str_negative = 'aabcde'

print(test_str_positive)
print(unique_char(test_str_positive))
print(test_str_negative)
print(unique_char(test_str_negative))
