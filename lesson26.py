def hi():
    print(888)
    return 333

print(hi())


# function with Positional args
def fp(a, b, c):
    print(a, b, c)

fp(3, 6, 55)


# function with Named args
def fn(a, b, c='pp'):
    print(a, b, c)

fn(3, 6)


# function with Uncounted positional args
def fup(*args):
    print(args)

fup(3, 6)


# function with Uncounted named args
def fun(**kwargs):
    print(kwargs)

fun(a = 3, x = 6)