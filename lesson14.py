# for i in range(1, 10):
#     print(f'Multipliction table for \033[1m{i}\033[0m')
#     for j in range (1, 11):
#         print(f'{i} * {j} = {i * j}')
# else:
#     print('Well done')


for i in range(1, 10):
    for j in range (2, 11):
        print(f'{i} * {j} = {i * j}\t', end = '')
    print('')
else:
    print('Well done')



# l1 = [i for i in 'Hello world' if i != ' ' and i != 'o']

# print(l1)
