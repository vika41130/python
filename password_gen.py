import random
import string

population = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pw_len = 8
def generate_password(population: str, pw_len: str) -> str:
    return ''.join(random.sample(population, pw_len))

# print(generate_password(population, pw_len))

def generate_password_2(population = string.ascii_letters + string.digits + string.punctuation, pw_len = 8) -> str:
    return ''.join(random.choice(population) for _ in range(pw_len))

print(generate_password_2())
