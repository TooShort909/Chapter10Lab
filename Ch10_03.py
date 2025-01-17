class Employee:
    def __init__(self, name, id_number, department, job_title):
        # Private attributes
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    # Accessor methods (getters)
    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    # Mutator methods (setters)
    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

# Program to create and display Employee objects
def main():
    # Create three Employee objects with provided data
    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    # Display information for each employee
    print("Employee 1:")
    print("Name:", employee1.get_name())
    print("ID Number:", employee1.get_id_number())
    print("Department:", employee1.get_department())
    print("Job Title:", employee1.get_job_title())
    print()

    print("Employee 2:")
    print("Name:", employee2.get_name())
    print("ID Number:", employee2.get_id_number())
    print("Department:", employee2.get_department())
    print("Job Title:", employee2.get_job_title())
    print()

    print("Employee 3:")
    print("Name:", employee3.get_name())
    print("ID Number:", employee3.get_id_number())
    print("Department:", employee3.get_department())
    print("Job Title:", employee3.get_job_title())

# Run the program
if __name__ == "__main__":
    main()
