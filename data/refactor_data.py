from faker import Faker

faker = Faker(locale="FR_fr")

class refactor_data:


    @staticmethod
    def add_employee():
        return {
            "firstName" : faker.first_name(),
            "lastName" : faker.last_name()
        }
