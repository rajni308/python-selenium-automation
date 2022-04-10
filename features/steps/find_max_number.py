#def find_max (n1, n2, n3):

    #return max(n1, n2, n3)
# n1= int(input('Input Value1: '))
# n2= int(input('Input Value2: '))
# n3= int(input('Input Value3: '))
 #print( find_max(n1, n2, n3))

def find_max(n1, n2, n3 ):
 if n1 > n2 and n1 > n3:
    return n1

 if n2 > n1 and n2 > n3:
    return n2
 return n3


n1= int(input('Input Value1: '))
n2= int(input('Input Value2: '))
n3= int(input('Input Value3: '))
print( find_max(n1, n2, n3))