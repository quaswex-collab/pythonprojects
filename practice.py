# # class Employee:
# #     def __init__(self, name, position, salary):
# #         self.name = name
# #         self.position = position
# #         self.salary = salary
        
# #     def introduce(self):
# #         print(f"Name: {self.name}")
# #         print(f"Position: {self.position}")
# #         print(f"Salary: {self.salary}")

# # Employee1 = Employee("Dawaa", "Web Developer", 10_000_000_000_000)
# # Employee1.introduce()


# # class Fruits:
# # 	def __init__(self, name, color, price):
# # 		self.name = name
# # 		self.color = color
# # 		self.price = price

# # 	def display_info(self):
# # 		print(f"Name: {self.name}")
# # 		print(f"Color: {self.color}")
# # 		print(f"Price: {self.price}")

# # Fruits1 = Fruits("apple", "red", 100)
# # Fruits1.display_info()

# class Gun:
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
        
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Color: {self.color}")
#         print(f"Price: {self.price}")

# Gun1 = Gun("Dessert eagle", "Grey", "750$")
# Gun1.display_info()

# class Animal:
#     def __init__(self, name, color, gender, energy = 100, hunger):
#         self.name = name
#         self.color = color
#         self.gender = gender
#         self.energy = energy
#         self.hunger = hunger
        
#     def information(self):
#         print(f"Speed: {self.name}. \nPower: {self.color}. \nHP: {self.gender}. \nEnergy: {self.energy}. \nHunger: {self.hunger}.")

# animal1 = Animal("Dolphin", "Sky blue", "Male", 100, "not that much")
# animal1.information()

class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed

    def accelerate(self, increase):
        self.speed += increase
        print(f"{self.brand} accelerated to {self.speed} km/h")

    def brake(self, decrease):
        self.speed -= decrease
        print(f"{self.brand} slowed down to {self.speed} km/h")

car1 = Car("Toyota", "Red", 60)
car2 = Car("BMW", "Black", 80)
car3 = Car("Tesla", "White", 100)

car1.accelerate(20)
car2.brake(30)
car3.accelerate(10)