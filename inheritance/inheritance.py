class Animal:
    alive = True

    def eat(self):
        print('This animal is eating')
    
    def sleep(self):
        print('This animal is sleeping')

class Rabit(Animal):
    pass

class Fish(Animal):
    pass

class Hawk(Animal):
    pass

rabit = Rabit()
fish = Fish()
hawk = Hawk()

fish.sleep