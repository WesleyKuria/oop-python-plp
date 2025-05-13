class Vehicle:
    def move(self):
        print("This vehicle is moving...")
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky! ")
class Car(Vehicle):
    def move(self):
        print("Driving on the road! ")
class Boat(Vehicle):
    def move(self):
        print("Sailing on the water! 🚢")
 # test
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
