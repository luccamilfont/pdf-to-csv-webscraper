import tabula
import pandas as pd
from pathlib import Path
import zipfile

pdfName = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csvName = "RolDeProcedimentos.csv"

with zipfile.ZipFile('Teste_pdfs.zip') as zipf:
    zipf.extract(pdfName)
    df = tabula.read_pdf(pdfName, encoding='utf-8', lattice=True, stream=False, pages="all")
    df = [i for i in df if not i.empty]

    for i in range(len(df)):
        df[i] = df[i].replace('OD', 'Seg. Odontológica')
        df[i] = df[i].replace('AMB', 'Seg. Ambulatorial')
    df = pd.concat(df)
    df.to_csv(csvName, index=False)
    Path(pdfName).unlink()
    
with zipfile.ZipFile('Teste_LuccaMilfont.zip', 'w') as zipf:
    zipf.write(csvName, csvName)
    Path(csvName).unlink()