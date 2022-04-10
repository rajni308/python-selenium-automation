def count_even_odd(n):
    even = 0 #or even =[]
    odd =0 #or odd= []
    while n!= 0:
        current_digit = n % 10
        if current_digit % 2:
            odd += 1 #or odd.append(current_digit)
        else:
            even += 1 #or even.append(current_digit)
        n = n // 10
    return ["Evens: " + str(even), "Odds: " + str(odd)]
number = int(input('Input a number:'))
print (count_even_odd(number))