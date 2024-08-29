import random
import string
import threading

class Aluno:
    """Classe Aluno com nome e idade."""

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #semelhante ao to String. Define como os alunos serão representados quando impressos
    def __repr__(self):  
        return f"Aluno(nome={self.nome}, idade={self.idade})"

    @staticmethod
    def gerar_aluno():
        """Gera um aluno com nome e idade aleatórios."""
        nome = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10))).capitalize() #pega
        idade = random.randint(18, 70)
        return Aluno(nome, idade)

class Util:
    """Classe com métodos estáticos para geração e manipulação de listas e arquivos."""

    @staticmethod
    def gerar_alunos(lista, quantidade):
        """Popula uma lista com Alunos com nomes e idades aleatórios.

        Args:
            lista (list): Lista onde os alunos serão armazenados.
            quantidade (int): Quantidade de alunos a serem gerados.
        """
        for _ in range(quantidade):
            lista.append(Aluno.gerar_aluno())

class Ordenacao:
    """Classe que contém métodos de ordenação para listas de Aluno."""

    @staticmethod
    def bolha(lista):
        """Ordena a lista de alunos usando o método de bolha por nome e idade."""
        houveTroca = True
        while houveTroca:
            houveTroca = False
            for i in range(len(lista) - 1):
                if (lista[i].nome > lista[i + 1].nome) or (lista[i].nome == lista[i + 1].nome and lista[i].idade > lista[i + 1].idade):
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    houveTroca = True

    @staticmethod
    def selecao(lista):
        """Ordena a lista de alunos usando o método de seleção por nome e idade."""
        for i in range(len(lista)):
            min_idx = i
            for j in range(i + 1, len(lista)):
                if (lista[j].nome < lista[min_idx].nome) or (lista[j].nome == lista[min_idx].nome and lista[j].idade < lista[min_idx].idade):
                    min_idx = j
            lista[i], lista[min_idx] = lista[min_idx], lista[i]

    @staticmethod
    def insercao(lista):
        """Ordena a lista de alunos usando o método de inserção por nome e idade."""
        for i in range(1, len(lista)):
            aux = lista[i]
            j = i - 1
            while j >= 0 and ((lista[j].nome > aux.nome) or (lista[j].nome == aux.nome and lista[j].idade > aux.idade)):
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = aux
