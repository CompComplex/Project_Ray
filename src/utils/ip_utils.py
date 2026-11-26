from random import randint
def generate_private_ip():
    octet1 = 10
    octet2 = randint(0,255)
    octet3 = randint(0,255)
    octet4 = randint(0,255)
    return f"{octet1}.{octet2}.{octet3}.{octet4}"