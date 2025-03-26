from bs4 import BeautifulSoup
import requests
from pathlib import Path
import zipfile

url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

tags = soup.find('main').select('a[href$=pdf][href*=Anexo]')

with zipfile.ZipFile('Teste_pdfs.zip', 'w') as zipf:
    for tag in tags:
        fileName = Path(tag['href'].split('/')[-1])
        pdfr = requests.get(tag['href'], stream=True)
        fileName.write_bytes(pdfr.content)
        zipf.write(fileName, fileName.name)
        fileName.unlink()

