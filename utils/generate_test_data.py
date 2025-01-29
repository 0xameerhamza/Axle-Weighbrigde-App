import random
import string
from faker import Faker

fake = Faker()

def generate_vehicle_registration():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    middle_digits = ''.join(random.choices(string.digits, k=2))
    last_digits = ''.join(random.choices(string.digits, k=3))
    registration_number = f"{letters}-{middle_digits}-{last_digits}"
    return registration_number

def generate_fake_name():
    return fake.name()

def generate_cnic():
    part1 = ''.join(random.choices('0123456789', k=5))
    part2 = ''.join(random.choices('0123456789', k=7))
    part3 = ''.join(random.choices('0123456789', k=1))
    cnic = f"{part1}-{part2}-{part3}"
    return cnic

def generate_phone_no():
    part1 = ''.join(random.choices('0123456789', k=2))
    part2 = ''.join(random.choices('0123456789', k=7))
    random_number = f"{part1}-{part2}"
    return random_number

def generate_weight():
    return random.randint(11, 30)