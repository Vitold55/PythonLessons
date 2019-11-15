# 1
def odd_ball(arr):
    i = arr.index('odd')
    return True if i in arr else False
    # if i in arr:
    #     return True
    # else:
    #     return False

print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"])) # True
print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"])) # False
print(odd_ball(["even",10,"odd",2,"even"])) # True


# 2
# def find_sum(n):
#     l = list(range(n + 1))
#     sum = 0
#
#     for i in l:
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#
#     return sum

def find_sum(n):
    return sum([i for i in list(range(n + 1)) if i % 3 == 0 or i % 5 == 0])

print(find_sum(5))
print(find_sum(10))

# 3
def get_names(names):
    return [name for name in names if len(name) == 4]

    # l2 = []
    # for name in names:
    #     if len(name) == 4:
    #         l2.append(name)
    #
    # return l2

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
print(get_names(names))
