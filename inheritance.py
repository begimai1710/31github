# Superclass
class Aircraft:

  def __init__(self, capacityC, capacityY, name):
    self.name = name
    self.capacityY = capacityY
    self.capacityC = capacityC


# Subclass
class Airbus(Aircraft):

  def get_capacityY(self):
    return self.capacityY

  def get_capacityC(self):
    return self.capacityC


# Subclass
class Boeing(Aircraft):

  def get_capacityC(self):
    return self.capacityC

  def can_carry_Y(self, passengers):
    return self.capacityC >= passengers


# Create instances of the subclasses
airbus_instance = Airbus(12, 126, "Airbus")
boeing_instance = Boeing(20, 130, "Boeing")

# Call the speak method on each instance
print(airbus_instance.name, airbus_instance.get_capacityC())
print(boeing_instance.name, boeing_instance.get_capacityC())
print(boeing_instance.can_carry_Y(20))
