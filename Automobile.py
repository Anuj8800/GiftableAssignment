class Automobile:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 90

    def brake(self):
        self.speed -= 20
        if self.speed < 0:
            self.speed = 0
        print(f"Brake applied: {self.brand} speed is {self.speed} km/h")
        
    def accelerate(self):
        self.speed += 20
        print(f"Accelerating: {self.brand} speed is {self.speed} km/h")

class Car(Automobile):
    def __init__(self, brand, model, gates):
        super().__init__(brand, model)
        self.gates = gates

    def emg_stop(self):
        print("Emergency!")
        self.brake() 

# run the code using their respective objects and methods
car1 = Car("BMW", "top", 4)
car1.brake()
car1.emg_stop()