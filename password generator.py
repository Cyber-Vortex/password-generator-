import random
import string

def generate_password(length=12):
    # Alphabet, numbers aur special characters ka mix
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# 12 characters ka password generate karna
print("Aapka Strong Password hai:", generate_password(12))
