from random import choices
from time import sleep

def fruity(interval=2):
    """Returns a fruit at a time interval"""

    fruit = ["apple", "cherry", "strawberry"]
    sleep(interval)
    return choices(fruit)