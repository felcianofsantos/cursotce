"""
Curso de introdução ao python
Aluno: Fernando Feliciano dos Santos

"""

# Importação de módulo

import calc
import entrada_saida

# Definição de funções

def main():
     lista_numeros = entrada_saida.entrada()
     operacao = input("""Qual operação você deseja?  Digite:
             + para adição,
             - para subtração,
             x - para multiplicação ou
             / para divisão\n""")
    
     if operacao == "+":
         valor = calc.adicao(lista_numeros[0], lista_numeros[1])
     elif operacao == "-":
         valor = calc.subtracao(lista_numeros[0], lista_numeros[1])
     elif operacao == "x":
         valor = calc.multiplicacao(lista_numeros[0], lista_numeros[1])
     elif operacao == "/":
         valor = calc.divisao(lista_numeros[0], lista_numeros[1])
     else:
         valor = "Esta operação não está definida para esta calculadora."
         entrad_saida.saida(valor)

if __name__ == "__main__":
      main() 