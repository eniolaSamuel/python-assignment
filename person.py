class Person:

    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age

    def set_name(self, first_name):
        self.first_name = "Eniola"

    def get_name(self):
        return self.first_name