class Flower:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Flower: {self.name}")

class Gardener:
    def __init__(self, name):
        self.name = name
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def show_flowers(self):
        print(f"{self.name}'s Flowers:")
        for flower in self.flowers:
            flower.show()

# Client code
gardener1 = Gardener("Alice")
gardener2 = Gardener("Bob")

gardener1.add_flower(Flower("Rose"))
gardener1.add_flower(Flower("Tulip"))

gardener2.add_flower(Flower("Lily"))

gardener1.show_flowers()
gardener2.show_flowers()
