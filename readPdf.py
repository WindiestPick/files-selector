from PyPDF2 import PdfReader


def lerPdf(caminho):
    reader = PdfReader(caminho)
    page = reader.pages[0]
    text = page.extract_text()
    return text

def getCPF(caminhoPdf):
    text = lerPdf(caminhoPdf)
    text = text.split("\n")
    text = text[13].split(" ")
    text = text[len(text) - 1]
    text = text.replace("-","")
    text = text.replace(".","")
    return text
