from btree import *
from util import *
import pickle


class Akinator:
    def __init__(self):
        self.tree = Tree(Node("", "", 1, None))
        self.tree.insert(Node("Deportes", "Deportes", 1, None))
        self.tree.insert(Node("Música", "Música", 1, None))
        self.name_file = "akinator.dat"

    def load_data(self):
        if os.path.isfile("./" + self.name_file):
            with open("./" + self.name_file, 'rb') as tree:
                self.tree = pickle.load(tree)

    def save_data(self):
        with open('akinator.dat', 'wb') as tree:
            pickle.dump(self.tree, tree)

    def game(self):
        user_response = get_option_int("Seleccione la temática:",
                                       (1, "Deportes"),
                                       (2, "Música")
                                       )
        node = self.tree.get("Deportes" if user_response == 1 else "Música")
        first_node = None
        if node.left and node.right:
            first_node = node.left if node.left.size > node.right.size else node.right
        else:
            first_node = node.left if node.left else node.right
        parent_node = self._game(first_node)
        self.insert_data(parent_node)
        user_confimation = get_confirmation("Desea jugar de nuevo?")
        if user_confimation:
            self.game()

    def _game(self, parent_node: Node):
        user_response = get_confirmation(f"{parent_node.value}?")
        if user_response and parent_node.type == ANSWER:
            print("JÁ, Gané")
            return parent_node
        else:
            if not parent_node.right and not parent_node.left:
                print(
                    "JÁ, Gané" if user_response and parent_node.type == ANSWER
                    else "No logré adivinar...\nHas ganado, Felicidades!!!")
                return parent_node
            if not parent_node.left and parent_node.right:
                return self._game(parent_node.right)
            if not parent_node.right and parent_node.left:
                return self._game(parent_node.left)
            if (parent_node.left.type == ANSWER and parent_node.right.type == ANSWER) or \
                    (parent_node.left.type == QUESTION and parent_node.right.type == QUESTION):
                return self._game(
                    parent_node.left if parent_node.left.size > parent_node.right.size else parent_node.right)
            if parent_node.left.type == ANSWER and parent_node.right.type == QUESTION:
                return self._game(parent_node.left if user_response else parent_node.right)
            if parent_node.right.type == ANSWER and parent_node.left.type == QUESTION:
                return self._game(parent_node.right if user_response else parent_node.left)

    def insert_data(self, parent_node):
        user_confirmation = get_confirmation("Desea agregar un nuevo dato?")
        if user_confirmation:
            answer = get_string("Ingrese el dato deseado")
            question = get_string("Ingrese un rasgo particular del dato anterior")
            self.tree.insert_question(question, answer, parent_node)
            self.save_data()

    def print_data(self):
        return self.tree.print()

    def interchange_data(self):
        self.print_data()
        try:
            option = get_option_int("Seleccione que acción desea ejecutar:",
                                    (1, "Insertar un dato a otro"),
                                    (2, "Intercambiar datos")
                                    )
            message1 = "Ingrese el primer dato a cambiar" if option == 2 else "Ingrese el dato que almacenará el otro"
            message2 = "Ingrese el segundo dato a cambiar" if option == 2 else "Ingrese el dato a almacenar"

            node1 = self.tree.get(get_string(message1))
            node2 = self.tree.get(get_string(message2))
            if option == 2:
                self.tree.interchange_nodes(node1, node2)
            elif option == 1:
                self.tree.insert_node_to_another(node1, node2)
            input("Presione cualquier tecla para ver los resultados...")
            clean_screen()
            self.print_data()
            self.save_data()
        except:
            print("Hubo un error")
