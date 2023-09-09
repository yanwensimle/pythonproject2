class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal):
    animal.speak()


dog = Dog()
cat = Cat()
make_noise(cat)
make_noise(dog)
