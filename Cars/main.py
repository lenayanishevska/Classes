from Cars.Car import Car

try:
    new_car = Car("BMW", "i7", 2020, 50)

    new_car.accelerate()
    new_car.accelerate()
    new_car.accelerate()
    new_car.display_speed()

    new_car.brake()
    new_car.brake()
    new_car.display_speed()

except Exception as e:
    print(f"Error: {e}")
