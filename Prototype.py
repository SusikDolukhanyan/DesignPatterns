import copy

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def clone(self):
        return copy.deepcopy(self)


original_character = Character("Luntik", 100, 15)
new_character = original_character.clone()
new_character.name = "Luntik mladshiy"
new_character.health = 80
new_character.attack = 20

print(f"Original Character: {original_character.name}, Health: {original_character.health}, Attack: {original_character.attack}")
print(f"Cloned Character: {new_character.name}, Health: {new_character.health}, Attack: {new_character.attack}")
