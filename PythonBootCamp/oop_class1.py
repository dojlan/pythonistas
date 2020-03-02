class Dog2():

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self, breed, name):

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # Expect spots to be a boolean True/False
        #self.spots = spots

    # OPERATIONS/ACTIONS ---> Methods
    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))


my_dog = Dog2('Lab', 'Frankie')
print(my_dog.species)
print(my_dog.breed)
print(my_dog.name)
my_dog.bark(8)



class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius ** 2 * Circle.pi

    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(6)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumference())


class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    # Overwriting an existing attribute
    def who_am_i(self):
        print("I am a dog!")

    def bark(self):
        print("WOOF!")

mydog = Dog()
mydog.who_am_i()
mydog.bark()

class Dog3():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Woof!"


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Meow!"

niko = Dog3("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)



class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

b = Book('Python rocks', 'Jose', 200)
print(b)
print(len(b))
del b
b