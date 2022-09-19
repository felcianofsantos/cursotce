import requests, csv

def leitura_csv(url):

    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        df = csv.reader(decoded_content.splitlines(), delimiter=',')
        
        return df