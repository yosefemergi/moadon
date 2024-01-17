class Person:
    def __init__(self, first , last):
        self.first = first
        self.last = last

    def full_name(self):
        print(self.first + " " + self.last)

new_person = Person("yosef","emergi")
new_person.full_name()