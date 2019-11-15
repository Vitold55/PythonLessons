def get_sum(a, b):
    """
    Function return sum of 2 elements a and b (Example of function comments)

    :param a: First param
    :type a: int
    :param b: Second param
    :type b: int
    :return: Return Int value
    """

    return a + b


print(get_sum(1, 5))


a = 5
# To change global variable - use "global" keyword
def f():
    global a
    a += 4

    return a