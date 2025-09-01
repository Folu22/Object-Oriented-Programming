# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def charge(self):
        return f"{self.brand} {self.model} is charging..."

    def info(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}mAh"


# Child Class with inheritance 
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    def play_game(self, game):
        return f"{self.brand} {self.model} is playing {game} on {self.gpu} GPU!"

    # Example of polymorphism (overriding method)
    def charge(self):
        return f"{self.brand} {self.model} supports fast charging ⚡!"


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 5000)
phone2 = GamingPhone("Asus", "ROG 7", 512, 6000, "Adreno 740")

print(phone1.info())
print(phone1.call("08123456789"))
print(phone1.charge())

print(phone2.info())
print(phone2.play_game("PUBG"))
print(phone2.charge())  # polymorphism in action
