import requests, csv
import pandas as pd
import urllib
from openpyxl import Workbook, load_workbook
import leitura_csv
import escrita_csv

def main():
	    CSV_URL = 'http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv'
	    dados = leitura_csv(CSV_URL)
	    lista = list(dados)
	    escrita_csv()
	    balancete = pd.read_csv('balancete.csv')
	    balancete.to_excel('balancete.xlsx')
	    novo_balancete = load_workbook('balancete.xlsx')
	    novo_balancete.save('novo_balancete.xlsx')
	

if __name__ =="__main__":

   main()
