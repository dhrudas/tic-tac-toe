
def is_perfect(n):
    sum_of_factors = 0
    for f in range(1,n):
        if n%f == 0:
            #print("Factor of ", n, "is", f )
            sum_of_factors = sum_of_factors + f
            #print(sum_of_factors)

    #if the sum of the factors is the input value
      #  then it is a perfect number

    if sum_of_factors == n:
        return True
    return False


for n in range( 38000000, 39000000):
    if is_perfect(n):
        print(n, " is perfect number")
