# 1
# a = [1, 2, 3]

# b = [i * 2 for i in a]

# print(a, b)


# 2
# l = [1, 2, 3]
# s = 0
# for j in l:
#     s += j ** 2

# print(s)


# 3
# time1 = int(3 * 0.5)
# time2 = int(6.7 * 0.5)
# time3 = int(11.8 * 0.5)

# print(time1, time2, time3)


# 4
s = 'Hello world'
# for i in s:
#     if i == ' ':
#         s1 = s.upper()
#         break
#     else:
#         s1 = s.lower()

if ' ' in s:
    s1 = s.upper()
else:
    s1 = s.lower()

print(s1)