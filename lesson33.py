# f = open('folder/file1.txt', 'r', encoding='UTF-8')
f = open('folder/file1.txt', 'a+', encoding='UTF-8')

# text = f.read()
# text1 = f.readline()
# text2 = f.readline()
# text3 = f.readline()
# text4 = f.readlines()

f.write('LOL\n')
text = f.read()

# print(text1)
# print(text2)

f.close()

print(text)