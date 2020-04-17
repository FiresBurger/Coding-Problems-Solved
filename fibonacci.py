import math
#using benet's formula
#Complexity O(1)
def fibonacci(n):
    return round(((pow(((1+math.sqrt(5))/2),n) - pow(((1-math.sqrt(5))/2),n))/math.sqrt(5)))

print(fibonacci(6))
