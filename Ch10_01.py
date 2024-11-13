class Car:
    def __init__(self, year_model, make):
        # Private attributes
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Method to accelerate the car (increases speed by 5)
    def accelerate(self):
        self.__speed += 5

    # Method to brake the car (decreases speed by 5)
    def brake(self):
        
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    
    def get_speed(self):
        return self.__speed

# Program to demonstrate the Car class
def main():
    
    car = Car(2023, "Toyota")

   
    print("Accelerating:")
    for _ in range(5):
        car.accelerate()
        print("Current speed:", car.get_speed())

  
    print("\nBraking:")
    for _ in range(5):
        car.brake()
        print("Current speed:", car.get_speed())

# Run the program
if __name__ == "__main__":
    main()