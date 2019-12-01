class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return "{} age is {}".format(self.name, self.age)
per=Person("Andry","29")
print(per.info())


