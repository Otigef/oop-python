import random

class Superhero:
    ENERGY_COST = 10  # Class attribute for energy cost

    def __init__(self, name, alias, powers, energy_level=100):
        self.name = name
        self.alias = alias
        self.powers = powers
        self.__energy_level = energy_level  # Encapsulated attribute

    def use_power(self):
        if not self.powers:
            print(f"{self.alias} has no powers to use!")
            return
        power = random.choice(self.powers)
        print(f"{self.alias} uses {power}!")
        self.__energy_level -= self.ENERGY_COST
        print(f"Energy decreased by {self.ENERGY_COST}. Now at {self.get_energy()}%")

    def recharge(self, amount):
        self.__energy_level += amount
        if self.__energy_level > 100:
            self.__energy_level = 100
        print(f"{self.alias} recharged! Energy now at {self.__energy_level}%")

    def get_energy(self):
        return self.__energy_level

class TechHero(Superhero):
    ENERGY_COST = 5  # Override energy cost for TechHero

    def __init__(self, name, alias, powers, energy_level, suit_model):
        super().__init__(name, alias, powers, energy_level)
        self.suit_model = suit_model  # Additional attribute

    def use_power(self):
        print(f"{self.alias} activates the {self.suit_model} suit! 💻")
        super().use_power()  # Calls the base class method with reduced energy cost

# Example usage
thor = Superhero("Thor Odinson", "Thor", ["Thunder strikes ⚡", "Storm summoning 🌪️"], 80)
iron_man = TechHero("Tony Stark", "Iron Man", ["Repulsor beams 🔫", "Rockets 🚀"], 90, "Mark XLIV")

thor.use_power()  # Output: Uses a random power and reduces energy by 10
iron_man.use_power()  # Output: Activates suit and reduces energy by 5
iron_man.recharge(20)  # Output: Recharges energy by 20