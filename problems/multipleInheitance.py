class Animal:
    def __init__(self,species):
        self.species = species
    def make_sound(self):
        pass
class CanFly:
    def fly(self):
        return "fly high"

class Bird(Animal,CanFly):
    def __init__(self,name,species):
        super().__init__(species)
        self.name = name
    def makeSound(self):
        return "chirp"
    

bird1 = Bird("robin","bird")
print(bird1.name)
print(bird1.species)


# a = lambda x,y: x*y
# print(a(7,8))