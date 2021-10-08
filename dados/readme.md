## Sobre os dados
Os dados utilizados para exemplificar o uso do **SigefScraper** foram obtidos dos arquivos shp baixados no [site do Incra](https://certificacao.incra.gov.br/csv_shp/export_shp.py). Exportei os arquivos da camada `Imóvel Certificado Sigef Privado` do estado de São Paulo. Mais detalhes sobre a certificação de imóveis rurais podem ser lidos no [manual do Sigef](https://sigef.incra.gov.br/documentos/manual/).

Para deixar o arquivo menos pesado, filtrei, através do [QGIS](https://qgis.org/pt_BR/site/), os imóveis com a situação `Área Titulada não Registrada`, situados no município de Cajamar (código do município no IBGE: 3509205). A relação de imóveis resultante conta com 9 registros. Exportei a [tabela de atributos](https://github.com/biamuniz/trabalhofinal_pensamentocomputacional/blob/main/dados/parcelas.csv) com as colunas descritas no dicionário de dados abaixo:

| **Coluna**  |  **Descrição**  |
| ------------------- | ------------------- |
|  parcela_co |  Código da parcela |
|  situacao_i |  Condição jurídica da área, que pode ser `Imóvel Registrado`, `Área Titulada não Registrada` ou `Área não Titulada` |
|  codigo_imo	 |  Código do imóvel no Sistema Nacional de Cadastro Rural (SNCR). Este código está disponível no Certificado de Cadastro de Imóvel Rural (CCIR)|
|  data_submi	|  Data de submissão |
|  data_aprov	|  Data de aprovação |
|  status	|  Status da certificação |
|  nome_area	|  Como o imóvel é chamado (nome de uma fazenda, por exemplo) |
|  municipio_	|  Código do município no IBGE |
|  uf_id |  Código da unidade federativa no IBGE |
