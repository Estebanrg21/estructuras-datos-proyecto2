import os


def get_int(message="Ingrese un número"):
    can_continue = False
    value = 0
    while not can_continue:
        try:
            value = int(input(message + "\n"))
            can_continue = True
        except:
            print("Por favor ingrese un value válido")
    return value


def get_option_int(message, *args):
    options_ids = []
    total_message = message + "\n"
    for option in args:
        if option is not None:
            total_message += f"{option[0]}- {option[1]}\n"
            options_ids.append(option[0])
    total_message += "Elija una de las anteriores:\n"
    option = None
    while option not in options_ids:
        option = get_int(total_message)
    return option


def get_confirmation(message):
    result = get_option_int(message, (1, "Sí"), (0, "No"))
    return result == 1


def clean_screen():
    try:
        os.system("cls")
    except:
        pass

def get_string(message):
    result = ""
    while result == "":
        result = input(message+"\n")
    return result