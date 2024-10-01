#1 - Vinicius Sobreira Borges / RM: 97767
#2 - Guilherme Catelli Bichaco / RM: 97989
#3 - Enzo de Oliveira Cunha / RM: 550985
#4 - Lucas Moreno Matheus / RM: 97158

class SimulacaoNode:
    def __init__(self, IdUsuario, procedimento, tempo, erros, feedback):
        self.IdUsuario = IdUsuario
        self.procedimento = procedimento
        self.tempo = tempo
        self.erros = erros
        self.feedback = feedback
        self.left = None  # Filho à esquerda
        self.right = None  # Filho à direita

class SimulacaoABB:
    def __init__(self):
        self.root = None  # Raiz da árvore

    # Inserindo um novo nó de simulação na árvore
    def inserir(self, IdUsuario, procedimento, tempo, erros, feedback):
        novo_nodo = SimulacaoNode(IdUsuario, procedimento, tempo, erros, feedback)
        if self.root is None:
            self.root = novo_nodo
        else:
            self._inserir_recursivo(self.root, novo_nodo)

    def _inserir_recursivo(self, current_node, novo_nodo):
        if novo_nodo.IdUsuario < current_node.IdUsuario:
            if current_node.left is None:
                current_node.left = novo_nodo
            else:
                self._inserir_recursivo(current_node.left, novo_nodo)
        else:
            if current_node.right is None:
                current_node.right = novo_nodo
            else:
                self._inserir_recursivo(current_node.right, novo_nodo)

    # Função para buscar uma simulação pelo ID do usuário
    def buscar(self, IdUsuario):
        return self._buscar_recursivo(self.root, IdUsuario)

    def _buscar_recursivo(self, current_node, IdUsuario):
        if current_node is None:
            return None
        if current_node.IdUsuario == IdUsuario:
            return current_node
        elif IdUsuario < current_node.IdUsuario:
            return self._buscar_recursivo(current_node.left, IdUsuario)
        else:
            return self._buscar_recursivo(current_node.right, IdUsuario)

    # Função para exibir as simulações em ordem (ID crescente)
    def exibir_em_ordem(self, node):
        if node:
            self.exibir_em_ordem(node.left)
            print(f"ID: {node.IdUsuario}, Procedimento: {node.procedimento}, Tempo: {node.tempo} min, Erros: {node.erros}, Feedback: {node.feedback}")
            self.exibir_em_ordem(node.right)


# Criando a árvore binária de simulações
abb = SimulacaoABB()

# Inserindo os dados de simulações
abb.inserir(101, "Apendicectomia", 35, 2, 4)
abb.inserir(102, "Colecistectomia", 50, 1, 3)
abb.inserir(103, "Hernioplastia", 45, 0, 2)
abb.inserir(104, "Vasectomia", 30, 1, 3)
abb.inserir(105, "Histerectomia", 60, 2, 5)
abb.inserir(106, "Colecistectomia", 40, 0, 1)
abb.inserir(107, "Cirurgia de Hérnia", 55, 1, 2)
abb.inserir(108, "Cirurgia Bariátrica", 120, 3, 6)

# Solicitando o ID do usuário ao qual o sistema deve fazer a busca
id_input = int(input("Digite o ID do usuário que você quer buscar: "))

# Buscando um dado de simulação pelo ID do usuário
usuario = abb.buscar(id_input)

if usuario:
    print(f"Simulação encontrada para o ID {usuario.IdUsuario}:")
    print(f"Procedimento: {usuario.procedimento}, Tempo: {usuario.tempo} minutos, Erros: {usuario.erros}, Feedback: {usuario.feedback}")
else:
    print("Simulação não encontrada")

# Exibindo todas as simulações em ordem de ID
print("\nSimulações em ordem de ID:")
abb.exibir_em_ordem(abb.root)
