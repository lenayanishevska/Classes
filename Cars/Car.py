class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

        if self.speed < 0:
            raise Exception("Speed can not be negative")

    def display_speed(self):
        print(f"Current speed : {self.speed}")
