def find_two_lowest_elements(arr):
    arr.sort()
    return arr[:2]
test_list = [198, 3, 4, 9, 10, 9, 2]
print(find_two_lowest_elements(test_list))