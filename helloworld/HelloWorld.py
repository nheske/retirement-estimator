class HelloWorld:
    name = "HelloWorld"

    def __init__(self, age=0):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def age_one_year(self):
        self._age += 1


if __name__ == '__main__':
    helloWorld = HelloWorld()
    print("I'm a helloWorld!")
    helloWorld.set_age(5)
    print("i'm "+str(helloWorld.get_age()))
    helloWorld.age_one_year()
    print("i'm "+str(helloWorld.get_age()))