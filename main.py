import akinator
import util
if __name__ == '__main__':
    game = akinator.Akinator()
    game.load_data()
    while True:
        option = util.get_option_int("Bienvenido al juego de akinator\nSeleccione que acción desea ejecutar:",
                            (1,"Jugar"),
                            (2,"Ordenar elementos"),
                            (3, "Salir"))
        if option == 1:
            game.game()
        elif option == 2:
            game.interchange_data()
        elif option == 3:
            break
