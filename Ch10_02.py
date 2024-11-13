class Person:
    def __init__(self, name, address, age, phone_number):
        # Private attributes
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    # Accessor methods (getters)
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    # Mutator methods (setters)
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

# Program to create instances with fictional data
def main():
    # Creating three Person objects with fictional information
    person1 = Person("Alice Smith", "123 Elm St, Springfield", 30, "555-1234")
    person2 = Person("Clark Kent", "456 Oak Ave, Metropolis", 42, "555-5678")
    person3 = Person("Bruce Wayne", "789 Pine Rd, Gotham", 28, "555-8765")

    # Displaying information for each person
    print("Person 1:")
    print("Name:", person1.get_name())
    print("Address:", person1.get_address())
    print("Age:", person1.get_age())
    print("Phone Number:", person1.get_phone_number())
    print()

    print("Person 2:")
    print("Name:", person2.get_name())
    print("Address:", person2.get_address())
    print("Age:", person2.get_age())
    print("Phone Number:", person2.get_phone_number())
    print()

    print("Person 3:")
    print("Name:", person3.get_name())
    print("Address:", person3.get_address())
    print("Age:", person3.get_age())
    print("Phone Number:", person3.get_phone_number())

# Run the program
if __name__ == "__main__":
    main()
