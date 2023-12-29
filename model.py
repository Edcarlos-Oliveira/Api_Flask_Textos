# Bibliotecas Necessárias
import pandas as pd
import nltk
import unicodedata
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

# Download Necessários
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

class Pre_Processamento(object):
    def __init__(self, arquivo):
        self.arq = arquivo

    # Retorna o arquivo
    def getArquivo(self):
        return self.arq
        
    # Remoção caracteres especiais
    def getTxt_limpo(self):
        self.arq_limpo = unicodedata.normalize('NFKD', self.arq).lower().encode('ascii', errors='ignore').decode('utf-8')
        return (re.sub('[!/,.-_]', ' ', self.arq_limpo))

    # Tokenizando o texto
    def getTxt_dividir(self):
        self.arq_tk = word_tokenize(self.arq_limpo)
        return self.arq_tk

    # Stop - Words(remove as palavras desnecessárias para o entendimento do texto)
    def getRemove_palavras(self):
        self.stopW = stopwords.words('portuguese')
        self.arq_sw = [w for w in self.arq_tk if not w.lower() in self.stopW]
        return self.arq_sw 

    # Stemização (Preserva a raiz do verbo)
    def getRaiz_verbo(self):
        self.snow_stm = SnowballStemmer(language='portuguese')
        self.arq_ss = [self.snow_stm.stem(w) for w in self.arq_sw]
        return self.arq_ss