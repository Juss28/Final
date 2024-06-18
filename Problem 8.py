import random
import string

def generate_password(length=12):
    """Generate a random alphanumeric password."""
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a password of length 12
print(generate_password())
