class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.name} restaurant offers {self.cuisine_type} cuisine.")

class IceCreamStand(Restaurant):
    def __init__(self, name, flavors):
        super().__init__(name, "ice cream")
        self.flavors = flavors

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Example usage
#ice_cream_stand = IceCreamStand("Dolly's", ["strawberry", "vanilla", "chocolate"])
#ice_cream_stand.display_flavors()
