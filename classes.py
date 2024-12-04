from abc import ABC


class Animal(ABC):
    def __init__(self, name, number_of_legs, skin=None, sound=None):
        self.__name = name
        self.__number_of_legs = number_of_legs
        self.__skin = skin
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_number_of_legs(self):
        return self.__number_of_legs

    def get_skin(self):
        return self.__skin

    def set_skin(self, skin):
        self.__skin = skin

    def get_sound(self):
        return self.__sound

    def set_sound(self, sound):
        self.__sound = sound

    def skin(self):
        print(f"The skin of {self.__name} consists of {self.__skin}.")

    def __str__(self):
        return f"{self.get_name()} has {self.get_number_of_legs()} legs."


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name, 0, skin="scales", sound="blub")


class Reptile(Animal):
    def __init__(self, name, legs):
        super().__init__(name, legs, skin="scales")


class Mammal(Animal):
    def __init__(self, name, legs):
        super().__init__(name, legs, skin="fur or hair")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, 2, skin="feathers")


class Insect(Animal):
    def __init__(self, name):
        super().__init__(name, 6, skin="exoskeleton")


class Amphibian(Animal):
    def __init__(self, name, legs):
        super().__init__(name, legs, skin="slimy skin")


class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name, 4)
        self.set_sound("meow")

    def meow(self):
        return self.get_sound()


class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name, 4)
        self.set_sound("bark")

    def bark(self):
        return self.get_sound()


class Frog(Amphibian):
    def __init__(self, name):
        super().__init__(name, 4)
        self.set_sound("croak")

    def croak(self):
        return self.get_sound()


class Robin(Bird):
    def __init__(self, name):
        super().__init__(name)
        self.set_sound("chirp")

    def chirp(self):
        return self.get_sound()


class Clownfish(Fish):
    def __init__(self, name):
        super().__init__(name)


class Mouse(Mammal):
    def __init__(self, name):
        super().__init__(name, 4)
        self.set_sound("squeak")

    def squeak(self):
        return self.get_sound()


if __name__ == "__main__":
    animals = [
        Clownfish("Nemo"),
        Cat("Whiskers"),
        Dog("Rover"),
        Frog("Hoppy"),
        Robin("Red"),
    ]

    for animal in animals:
        print(animal)
        print(f"{animal.get_name()} says {animal.get_sound()}.")
