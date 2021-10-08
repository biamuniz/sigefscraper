# -*- coding: utf-8 -*-
"""sigefscraper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14tNA-FQ30PtXbS_5O5VK-7v_Ifle9egM

#<center> **SigefScraper: obtendo informações de imóveis certificados no Sigef com Python**</center>

**Objetivo**: A partir de uma relação de códigos de parcelas de imóveis certificados no Sigef (Sistema de Gestão Fundiária do Incra), saber quem são seus detentores.
"""

# Importando as bibliotecas necessárias
import pandas as pd
from urllib.request import urlopen #para lidar com os links
import ssl #para lidar com o certificado de segurança
ssl._create_default_https_context = ssl._create_unverified_context

# Lendo o banco de dados
df=pd.read_csv("parcelas.csv", sep=";")
# Criando uma coluna com o nome link que vai abrigar o link do detalhe da parcela
df['link'] = 'https://sigef.incra.gov.br/geo/parcela/detalhe/' + df['parcela_co']
df

# Olhando os links
for i in df['link']:
  print(i)

# Coletando o nome e o documento (CPF/CNPJ) dos detentores de cada parcela linkada
for i in list(df['link']):
  resposta = urlopen(i)
  html = resposta.read().decode("utf-8")
  partes = html.split("CPF/CNPJ</th>\n        </tr>\n        </thead>\n        <tbody>\n\n        \n\n            <tr>\n                <td>")
  for parte in partes:
    subparte = parte.split("</td>\n")
    nome = subparte[0]
    documento = subparte[1]
  print(nome)
  print(documento)