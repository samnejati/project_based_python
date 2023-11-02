import random

def generate_random_number(start:int, end: int)  -> int:  ## :int ->int : this is called type annotation
    """Generates a random number between start and end"""
    return random.randint(start, end)
