from faker import Faker

fake = Faker()

def generate_pseudonym():
    return fake.user_name()