class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(f"Item: {item}")

class MealBuilder:
    def build_main(self):
        pass

    def build_drink(self):
        pass

    def build_dessert(self):
        pass

    def get_meal(self):
        return self.meal


class VegMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def build_main(self):
        self.meal.add_item("Vegetable Curry")

    def build_drink(self):
        self.meal.add_item("Juice")

    def build_dessert(self):
        self.meal.add_item("Fruit Salad")


class MealDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_meal(self):
        self.builder.build_main()
        self.builder.build_drink()
        self.builder.build_dessert()


builder = VegMealBuilder()
director = MealDirector(builder)
director.construct_meal()
meal = builder.get_meal()
meal.show_items()
