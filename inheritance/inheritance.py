class Animal:
    alive = True

    def eat(self):
        print('This animal is eating')
    
    def sleep(self):
        print('This animal is sleeping')

class Rabit(Animal):
    def run(self):
        print('Rabit is running')

class Fish(Animal):
    def swim(self):
        print('Fish is swimming')

class Hawk(Animal):
    def fly(self):
        print('Hawk is flying')

rabit = Rabit()
fish = Fish()
hawk = Hawk()

fish.sleep() # This animal is sleeping
fish.swim() # Fish is swimming

# python.exe