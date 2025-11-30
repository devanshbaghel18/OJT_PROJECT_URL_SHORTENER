import string
import random

def generate_short_code(length=6):
    """Generates a random string of uppercase letters and digits."""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))