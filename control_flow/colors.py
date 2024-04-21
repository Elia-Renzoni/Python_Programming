#   @author Elia Renzoni
#   @date 21/04/2024
#   @brief enums in Python

from enum import Enum

class Colors(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

def matchColors():
    color = Colors(input("Insersci un colore :"))
    match color:
        case Colors.RED:
            return "Rosso !!"
        case Colors.BLUE:
            return "Blue !!"
        case Colors.GREEN:
            return "Green !!"
        case _:
            raise ValueError("Value Not Allowed !!")

print(matchColors())
