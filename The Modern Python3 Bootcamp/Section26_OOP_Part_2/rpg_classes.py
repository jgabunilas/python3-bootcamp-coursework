# Role-playing game classes exercise

# Character class (parent class)
class Character:
        def __init__(self, name, hp, level):
                self.name = name
                self.hp = hp
                self.level = level

# NPC subclass (child class)
class NPC(Character):
        def __init__(self, name, hp, level):
                # Initialize based on the parent character class
                super().__init__(name, hp, level)
        
        def speak(self):
                return 'I used to be an adventurer like you, but then I took an arrow to the knee.'

villager = NPC("Bob", 100, 12)
print(villager.name)
print(villager.hp)
print(villager.level)
print(villager.speak())