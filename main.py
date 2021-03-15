from time import perf_counter


class Vaccine:

    def __init__(self, vaccine, date):
        self.vaccine = vaccine
        self.date = date


class Node:

    def __init__(self, num_utente, vaccine):
        self.num_utente = num_utente  # o nome é a key
        self.vaccines = [vaccine]  # lista de vacinas (classe)
        self.left = None
        self.right = None
        self.h = 1  # altura


class AVLTree:

    def insert(self, node, num_utente, vaccine_input, date_input):

        if not node:
            print("NOVO UTENTE CRIADO")
            return Node(num_utente, Vaccine(vaccine_input, date_input))

        elif num_utente < node.num_utente:
            node.left = self.insert(node.left, num_utente, vaccine_input, date_input)

        elif num_utente > node.num_utente:
            node.right = self.insert(node.right, num_utente, vaccine_input, date_input)

        if num_utente == node.num_utente:
            flag = 1
            for vaccine in node.vaccines:
                if vaccine_input == vaccine.vaccine:
                    vaccine.date = date_input
                    print("VACINA ATUALIZADA")
                    flag = 0
            if flag == 1:
                node.vaccines.append(Vaccine(vaccine_input, date_input))
                print("NOVA VACINA INSERIDA")

        node.h = 1 + max(get_h(node.left), get_h(node.right))  # update altura do nó pai
        return rebalance(node, num_utente)  # equilibra a árvore, se necessário

    def listing(self, node):

        count = 0
        if not node:
            return
        self.listing(node.left)

        for vac in sorted(node.vaccines, key=lambda x: x.vaccine):
            if count == 0:
                print(f"{node.num_utente}", end="")
                count += 1
            print(f" {vac.vaccine} {vac.date}", end="")
        print()

        self.listing(node.right)

    def consult(self, node, num_utente):

        if node is None:
            return False
        elif num_utente == node.num_utente:
            for vac in node.vaccines:
                print(f"{vac.vaccine} {vac.date}")
                return True
        elif num_utente > node.num_utente:
            return self.consult(node.right, num_utente)
        return self.consult(node.left, num_utente)

    def delete_tree(self, node):

        if node is not None:
            self.delete_tree(node.left)
            self.delete_tree(node.right)
            node.left = None
            node.right = None


def get_h(node):  # devolve a altura do nó

    if not node:  # Se o nó não existir
        return 0
    return node.h


def get_fe(node):  # devolve o fator de equilíbrio do nó

    if not node:  # Se o nó não existir
        return 0
    return get_h(node.left) - get_h(node.right)


def left_rotation(root_node):
    
    new_root_node = root_node.right
    undock_node = new_root_node.left  # o nó que vai desencaixar está à esquerda do nó filho direito do nó principal

    new_root_node.left = root_node  # o nó principal faz a rotação para a direita, fica no lugar do undock_node
    root_node.right = undock_node

    root_node.h = 1 + max(get_h(root_node.left), get_h(root_node.right))
    new_root_node.h = 1 + max(get_h(new_root_node.left), get_h(new_root_node.right))

    return new_root_node


def right_rotation(root_node):

    new_root_node = root_node.left
    undock_node = new_root_node.right

    new_root_node.right = root_node
    root_node.left = undock_node

    root_node.h = 1 + max(get_h(root_node.left), get_h(root_node.right))
    new_root_node.h = 1 + max(get_h(new_root_node.left), get_h(new_root_node.right))

    return new_root_node


def rebalance(node, num_utente):

    if get_fe(node) > 1 and num_utente < node.left.num_utente:  # Esquerda predominante
        return right_rotation(node)
    if get_fe(node) > 1 and num_utente > node.left.num_utente:  # Esquerda + subdireita predominante
        node.left = left_rotation(node.left)
        return right_rotation(node)

    if get_fe(node) < -1 and num_utente > node.right.num_utente:  # Direita predominante
        return left_rotation(node)
    if get_fe(node) < -1 and num_utente < node.right.num_utente:  # Direita + subesquerda predominante
        node.right = right_rotation(node.right)
        return left_rotation(node)

    return node


tree = AVLTree()
root = None

total_time = 0

while True:

    inputs = [i for i in input().split()]

    if inputs[0].lower() == "acrescenta":
        tik = perf_counter()
        root = tree.insert(root, int(inputs[1]), inputs[2], inputs[3])
        tok = perf_counter()
        total_time += tok - tik

    elif inputs[0].lower() == "consulta":
        tik = perf_counter()
        if not tree.consult(root, int(inputs[1])): print("NÃO ENCONTRADO")
        tok = perf_counter()
        total_time += tok - tik

    elif inputs[0].lower() == "lista":
        tree.listing(root)

    elif inputs[0].lower() == "apaga":
        tree.delete_tree(root)
        root = None
        print("LISTAGEM DE NOMES VAZIA")
    elif inputs[0].lower() == "fim":
        print(total_time)
        break

