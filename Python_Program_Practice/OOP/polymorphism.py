def driver(car):
    car.drive()

class Creta:
    def drive(self):
        print("Creta is driving")
class Mercedes:
    def drive(self):
        print("Mercedes is driving")

c = Creta()
driver(c)