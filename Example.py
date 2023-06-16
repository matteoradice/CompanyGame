class NoResourcesError(Exception):
    def __init__(self):
        print("MINORE DI 0")

class MyCode:
    while True:
        try:
            resources = int(input("Insert resources: "))
            if resources <= 0:
                raise NoResourcesError
        except ValueError:
            print("Non hai inserito un numero")
        except NoResourcesError:
            break
        else:
            print("A buon fine")
            break
    print("CICLO TERMINATO")

myCode = MyCode()
