#code to sum the squares of a number in a array

test_list = [3, 5, 7, 9, 11]
 
# sum of squares

res = 0

for i in test_list:

    from math import pow

    res += pow(i, 2)

res = int(res)
# printing result

print("The sum of squares of list is : " + str(res))
