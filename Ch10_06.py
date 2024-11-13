class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):

        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone = emergency_contact_phone


    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_phone_number(self):
        return self.__phone_number

    def get_emergency_contact_name(self):
        return self.__emergency_contact_name

    def get_emergency_contact_phone(self):
        return self.__emergency_contact_phone

class Procedure:
    def __init__(self, procedure_name, date, practitioner, charges):

        self.__procedure_name = procedure_name
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges


    def get_procedure_name(self):
        return self.__procedure_name

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges


# Program to create and display patient and procedure information
def main():

    patient = Patient(
        first_name="John",
        middle_name="A.",
        last_name="Doe",
        address="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345",
        phone_number="555-1234",
        emergency_contact_name="Jane Doe",
        emergency_contact_phone="555-5678"
    )

    procedure1 = Procedure("Physical Exam", "2024-11-13", "Dr. Irvine", 250.00)
    procedure2 = Procedure("X-ray", "2024-11-13", "Dr. Jamison", 500.00)
    procedure3 = Procedure("Blood test", "2024-11-13", "Dr. Smith", 200.00)

    print("Patient Information:")
    print("Name:", patient.get_first_name(), patient.get_middle_name(), patient.get_last_name())
    print("Address:", patient.get_address(), patient.get_city(), patient.get_state(), patient.get_zip_code())
    print("Phone Number:", patient.get_phone_number())
    print("Emergency Contact:", patient.get_emergency_contact_name(), "| Phone:", patient.get_emergency_contact_phone())
    print()

    # Display Procedure Information and calculate total charges
    print("Procedures:")
    total_charges = 0

    for procedure in [procedure1, procedure2, procedure3]:
        print("Procedure Name:", procedure.get_procedure_name())
        print("Date:", procedure.get_date())
        print("Practitioner:", procedure.get_practitioner())
        print("Charges: $", format(procedure.get_charges(), ".2f"), sep="")
        total_charges += procedure.get_charges()
        print()

    print("Total Charges for all procedures: $", format(total_charges, ".2f"), sep="")

# Run the program
if __name__ == "__main__":
    main()