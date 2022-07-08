from data.data import Person
from faker import Faker

faker_en = Faker("ru_RU")
Faker.seed()


def person_generator():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
    )