class A:
    def __init__(self, name):
        # Class constructor
        self.name = name

    def get_info(self):
        print("Hello, " + self.name)

    def __del__(self):
        # Class destructor
        del self.name


a1 = A('Vilan')
a1.get_info()
a2 = A('Roman')
a2.get_info()