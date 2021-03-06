## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name
    
## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None
    
    def b(self):
        print self.name + " breathing in and out."

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salery):
        ## Employee is-a Person which has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salery
        self.salery = salery

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

print "Test"

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")
mary.b()

## Mary has-a Pet named Satan
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)
frank.b()

## Frank has-a Pet named Rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()

