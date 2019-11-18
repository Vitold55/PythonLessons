# Lambda functions

get_square = lambda num: num ** 2 # Not preferabl method of using lambda
print(get_square(9))

# Second variant of using
print((lambda n: n ** 3)(3))

# Preferable method of usage
l = [1, 2, 3, 4]
l2 = list(map(lambda i: i * 2, l))
print(l2)