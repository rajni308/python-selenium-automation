#def sum(n):
  #  final_result =0
  #  for x in range (1, n+1):
    #    final_result = final_result+x5

   # return final_result

# number = int(input('Input a number:'))
def sum(n):
    final_result = (n * (n+1))/2
    return final_result
number = int(input('Input a number:'))
print(sum(number))