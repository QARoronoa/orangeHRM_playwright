from faker import Faker

faker = Faker(locale="FR_fr")

class refactor_data:


    @staticmethod
    def add_employee():
        return {
            "firstName" : "ussop",
            "firstNameEmpty": "",
            "firstName2": faker.first_name(),
            "lastName" : "hammer"
        }
