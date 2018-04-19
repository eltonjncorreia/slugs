import re
from unicodedata import normalize


def create_slug(texto):
    expressao = re.compile(r'\W+')
    texto_sem_acentos = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    texto_sub = expressao.sub('-', texto_sem_acentos).lower()
    return texto_sub


