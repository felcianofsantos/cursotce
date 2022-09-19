import csv

def escrita_csv(nome_csv,lista):
    with open('nome_csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(lista)