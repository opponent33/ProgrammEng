class Icecream:
    def __init__(self, ingredient = None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None
    def composition(self):
        if self.ingredient:
            print(f"Icecream with {self.ingredient}")
        else:
            print("common Icecream")

icecream = Icecream()
icecream.composition()
icecream = Icecream("Chocolate")
icecream.composition()
icecream = Icecream(5)
icecream.composition()