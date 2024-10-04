#   @author Elia Renzoni
#   @date 21/04/2924
#   @brief default arguments values in Python functions

def ask(initMessage, reminder="Please, Try Again !"):
    """ brief info """
    while True:
        value = input(initMessage)
        if value in {"y", "yes", "si", "sì"}:
            return True
        elif value in {"n", "no", "nope"}:
            return False
        else:
            raise ValueError("****")
    print(reminder)

def check(valueReturned):
    match valueReturned:
        case True:
            print("Bravo!")
        case False:
            print("Male !")


check(ask("Hai Mangiato ?"))

