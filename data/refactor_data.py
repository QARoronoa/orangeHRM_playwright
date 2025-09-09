from faker import Faker

faker = Faker(locale="FR_fr")

class refactor_data:


    @staticmethod
    def add_employee():
        return {
            "firstName" : faker.first_name(),
            "firstName2": " ",
            "lastName" : faker.last_name()
        }
