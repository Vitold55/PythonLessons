# Decorators
def show_info():
    print('My name is Viktor')

def simple_decorator(func):
    def wrapped():
        print('Before decorate')
        func()
        print('After decorate')
    return wrapped

simple_decorator(show_info)()


# Decorate to Capitalize first letter and delete , (function without arguments)
def create_title0(func):
    def wrapped():
        title = func()
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapped

@create_title0
def show_title0():
    return 'hello, world!!!'


print(show_title0())


# Decorate to Capitalize first letter and delete , (function with arguments)
def create_title(func):
    def wrapped(*args):
        title = func(*args)
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapped

@create_title
def show_title(title):
    return title


print(show_title('hello, my dear friend'))