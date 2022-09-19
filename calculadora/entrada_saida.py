"""
FUNÇÕES DE ENTRADA E SAÍDA
"""


def entrada() -> list:
    """
     Escrever a docstring da função
    """
    num_1 = float(input("Digite o primeiro número: "))
    num_2 = float(input("Digite o segundo número: ")) 
  return [num_1, num_2]


def saida(valor: float):
    """
     Escreva o docstring
    """
      print(f"O resultado da operação é igual a {valor}")
