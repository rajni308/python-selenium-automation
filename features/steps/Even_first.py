def even_first(arr):
     next_even, next_odd = 0, len(arr) -1
     while next_even < next_odd:
      if arr [next_even] % 2 == 0:
        next_even += 1

      else:
        arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
        next_odd -= 1

test_arr = [7, 3, 5, 6, 4, 10, 3, 2]
print(test_arr)
even_first(test_arr)
print(test_arr)
