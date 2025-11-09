from typing import Type
import random



class Pet:
    def __init__(self, name: str):
        self.name = name


    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError



class Dog(Pet):
    def speak(self) -> None:
        print("Woof")

    def __str__(self) -> str:
        return f"Dog <{self.name}>"



class Cat(Pet):
    def speak(self) -> None:
        print("Meow")

    def __str__(self) -> str:
        return f"Cat <{self.name}>"




class PetShop:
    def __init__(self, animal_factory: Type[Pet]):
        self.pet_factory = animal_factory


    def buy_pet(self, name: str) -> Pet:
        pet = self.pet_factory(name)
        print(f"Here is your lovely {pet}")
        return pet



if __name__ == "__main__":
    animals = [Dog, Cat]
    random_animal: Type[Pet] = random.choice(animals)
    shop_pet = PetShop(random_animal)
    shop_pet.buy_pet("Max")
    import doctest
    doctest.testmod()