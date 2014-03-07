class Person():
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print('Person - ')
        return ('My name is {0}. I am {1} years old.'. format(self.name, self.age))

class Military(Person):
    def __init__ (self, name, age, rank):
        Person.__init__(self, name, age)
        self.rank = rank

    def __str__(self):
        print('Military - ')
        return Person.__str__(self) + 'I am a {0}'.format(self.rank)
        

class Teacher(Person):
    def __init__(self, name, age, sub):
        Person.__init__(self, name, age)
        self.sub = sub

    def __str__(self):
        print('Teacher -')
        return 'my name is {0}i teach {1}' .format(self.name, self.sub)

class Student(Person):
    def __init__(self, name, age, loans):
        Person.__init__(self, name, age)
        self.loans = loans
