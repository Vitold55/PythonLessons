import os

def get_folder_tree(basefolder):
    tree = os.walk(basefolder)

    for root, subfolders, files in tree:
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        sub_indent = ' ' * 4 * (level + 1)

        print(indent + os.path.basename(root))

        for file in files:
            print(sub_indent + file)


get_folder_tree('folder')