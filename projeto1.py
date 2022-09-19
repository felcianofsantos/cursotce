import os 
import shutil
import os 



if os.path.exists("documentos")==False:
    os.mkdir("documentos")
if os.path.exists("planilhas")== False:
    os.mkdir("planilhas")
if os.path.exists("documentos")== False:
    os.mkdir("documentos")

arquivos=os.listdir()
for arquivo in arquivos:

    if ".xls" in arquivo:
        shutil.move(arquivo,f"./planilhas/{arquivo}")
    elif ".doc" in arquivo:
        shutil.move(arquivo,f"./documentos/{arquivo}") 
    elif ".pdf" in arquivo:
        shutil.move(arquivo,f"./documentos/{arquivo}")     

