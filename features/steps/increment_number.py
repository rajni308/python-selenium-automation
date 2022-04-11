def plus_one(arr):
    arr[-1] += 1
    for i in reversed (range(1, len(arr))):
        if arr[i]  != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1

    if arr[0] == 10:
         arr[0] = 1
         arr.append(0)
          # arr.insert(0, 1)
    return arr
test_arr_124 = [1, 2, 4]
test_arr_129 = [1, 2, 9]
test_arr_999 = [9, 9, 9]

print(plus_one(test_arr_124))
print(plus_one(test_arr_129))
print(plus_one(test_arr_999))