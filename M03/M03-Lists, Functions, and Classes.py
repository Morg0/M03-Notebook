 #Classes
class Vehicle:
    def __init__(self, vehicleType):
      self.vehicleType = vehicleType  

#child class automobile
class Automobile(Vehicle):
   def __init__(self, vehicleType, year, make, model, doors, roof):
      Vehicle().__init__()
      self.year = year
      self.make = make
      self.model = model
      self.doors = doors
      self.roof = roof

   def __str__(self) -> str:
       return "Vehicle Type: " + self.vehicleType + "\nYear: " + self

#input values
if __name__ ==  "__main__":
   #year of the car
   year = input("Enter your cars year: ")
   #cars make/brand
   make = input("Enter your cars make: ")
   #cars model
   model = input("Enter your cars model: ")
   #number of doors
   doors = input("Enter number of car doors (2 or 4): ")
   #if there is a roof or not
   roof = input("Enter your roof type (solid or sun roof): ")

print("Vehicle information")

