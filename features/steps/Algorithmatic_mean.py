def below_arithmetical_mean(arr):
    arithmetical_mean = sum(arr)/len(arr)
    print(f"arithmetical_mean{arithmetical_mean}")
    final_list = []
    for num in arr:
        if num < arithmetical_mean:
            final_list.append(num)
    return final_list
test_list = [1, 3, 5, 6, 4, 10, 2, 3]
print(below_arithmetical_mean(test_list))