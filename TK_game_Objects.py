import random

# Parent class
class Character:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def attack(self, target):           # target is also a Character object!
        damage = max(0, self.atk - target.defense)
        target.hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!\n")
        if target.hp <= 0:
            print(f"{target.name} has been defeated!\n")

    def show_status(self):
        pass

    def special_move(self, target):
        pass

# child class
class Hero(Character):
    def __init__(self, name, hp, atk, defense, role):
        super().__init__(name, hp, atk, defense)
        self.role = role.lower()

    def show_status(self):
        print(f"{self.name:10} | {self.hp:3} | {self.atk:3} | {self.defense:3} | ({self.role})")

    def special_move(self, target):
        if self.role == "healer":
            heal = random.randint(50, 60)
            target.hp += heal
            print(f"{self.name} uses Healing, restoring {heal} HP to {target.name}!\n")

        if self.role == "warrior":
            print(f"{self.name} uses Valor and deals triple damage!\n")
            damage = max(0, self.atk * 3 - target.defense)
            target.hp -= damage
            print(f"{self.name} attacks {target.name} for {damage} damage!\n")
            if target.hp <= 0:
                print(f"{target.name} has been defeated!\n")

# child class
class Monster(Character):
    def __init__(self, name, hp, atk, defense, role):
        super().__init__(name, hp, atk, defense)
        self.role = role.lower()

    def show_status(self):
        print(f"{self.name:10} | {self.hp:3} | {self.atk:3} | {self.defense:3} | ({self.role})")

    def special_move(self, target):
        if self.role == "boss":
            reduction = target.atk//2
            target.atk -= reduction
           #print(f"XXX")
            print(f"{self.name} lets out a mighty roar, intimidating {target.name} and reducing their attack by {reduction}!\n")


#A class that stores character(Hero/Monster) objects in a list
class CharacterList:
    def __init__(self):
        self.__characters = []  # a list

    # Add a character to the list
    def addCharacter(self, character):
        self.__characters.append(character)

    # Returns a character from the list
    def getCharacter(self, name):
        for character in self.__characters:
            a=character.name
            if a.lower()==name.lower():
                return character

    # Used to get a bool value: if name in names:
    def getCharacterNames(self):
        list=[]
        for i in self.__characters:
            list.append(i.name)
        return list

    # Removes a character from the list
    def removeCharacter(self, name):
        for character in self.__characters:
            a=character.name
            if a.lower()==name.lower():
                self.__characters.remove(character)
                

    # Returns the number of charachters in the list
    def getCount(self):
        return len(self.__characters)

    # the __iter__() method provides a way for other programs
    # to use a for loop to iterate through the items in the object
    def __iter__(self):
        for character in self.__characters:
            yield character

    # Displays characters info in a nice format
    def display_list(self):
        print(f"   {'Name':10} | {' HP':3} | {'ATK':3} | {'DEF':3} |  Role")
        for i, character in enumerate(self.__characters, start=1):
            print(f"{i}. ", end="")
            character.show_status()


