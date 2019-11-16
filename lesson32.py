import os

tree = os.walk('folder')

for root, subfolders, files in tree:
    level = root.count(os.sep)
    indent = ' ' * 4 * level
    sub_indent = ' ' * 4 * (level + 1)

    print(indent + os.path.basename(root))

    for file in files:
        print(sub_indent + file)