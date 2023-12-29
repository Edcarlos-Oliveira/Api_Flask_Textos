# Api_Flask_Textos
 Projeto Natural Language Toolkit (NLTK)

Código escrito no Jupyter Notebook:

#### Pré_Processamento de Textos:
- Realizado nesse projeto os seguintes passos:  
    - Criação do Objeto [ __Pré_Processamento__ ];
    - Função para remoção dos caracteres especiais, utilizando o métodos [ __*unicodedata.normalize*__];
    - A tokenização do texto será usado o método [ __*word_tokenize*__];
    - Para remover as palavras que não alteram o sentido do texto, usei o método [ __*stopwords.words*__];
    - Para 'pegar só o radical das palavras, utilizei o algoritmo [ __*SnowballStemmer*__].
- __OBJETIVO:__ - Facilitar o pré-processamento de textos ou palavras inicializando o objeto:

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

#### Criando o Objeto:
- Aqui serão criadas as funções para cada etapa do projeto.

class Pre_Processamento(object):
    def __init__(self, arquivo):
        self.arq = arquivo

    # Retorna o arquivo
    def getArquivo(self):
        return self.arq
        

    # Remoção caracteres especiais
    def getTxt_limpo(self):
        self.arq_limpo = unicodedata.normalize('NFKD', dados.getArquivo()).lower().encode('ascii', errors='ignore').decode('utf-8')
        return (re.sub('[!/,.-_]', ' ', self.arq_limpo))

    # Tokenizando o texto
    def getTxt_dividir(self):
        self.arq_tk = word_tokenize(dados.getTxt_limpo())
        return self.arq_tk

    # Stop - Words(remove as palavras desnecessárias para o entendimento do texto)
    def getRemove_palavras(self):
        self.stopW = stopwords.words('portuguese')
        self.arq_sw = [w for w in dados.getTxt_dividir() if not w.lower() in self.stopW]
        return self.arq_sw 

    # Stemização (Preserva a raiz do verbo)
    def getRaiz_verbo(self):
        self.snow_stm = SnowballStemmer(language='portuguese')
        self.arq_ss = [self.snow_stm.stem(w) for w in dados.getRemove_palavras()]
        print(f'O texto processado segue abaixo:\n{self.arq_ss}')

    # Chama todas as funções
    def main(self):
        #dados.getArquivo()
        #dados.getTxt_limpo()
        #dados.getTxt_dividir()
        #dados.getRemove_palavras()
        dados.getRaiz_verbo()

# Passando o parâmetro
arquivo = "Edcarlos Oliveira"

# Iniciando o objeto
if __name__ == '__main__':
    dados = Pre_Processamento(arquivo)
    print(dados.main())
	
#### Autor:
- __*Edcarlos Oliveira*__
- __GitHub:__ https://github.com/Edcarlos-Oliveira
