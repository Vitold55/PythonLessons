words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']

words0 = [i for i in words if i == i[::-1]]
words1 = []
for w in words:
    if w == w[::-1]:
        words1.append(w)

print(words0, words1)

my_str1 = []
for str in my_str:
    str_without_spaces = str.replace(' ', '').lower()
    if str_without_spaces == str_without_spaces[::-1]:
        my_str1.append(str)

print(my_str1)