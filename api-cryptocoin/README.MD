### Projeto de ETL realizado no bootcamp **"Engenharia de Dados"** da Stack Academy

### Objetivo:
  Consumir dados de uma API de criptomoedas (https://coinmarketcap.com/) e salvar na nuvem no Banco de Dados da Amazon RDS.
  
### Tecnologias
 - Python
 - Pandas (Biblioteca)
 - Requests (Biblioteca)
 - SQLAlchemy (Biblioteca)
 - JSON (Dados recebidos da API)
 - SGBD Postgres na Amazon RDS

### Arquitetura do Projeto
![Arquitetura](https://i.imgur.com/c5iuujB.png)

### Plano de Execução
  Consumir os dados da API do site CoinMarketCap (site que mostra as cotações de criptomoedas), armazenar os dados em um pandas Dataframe, realizar validações (resultados vazios ou nulos), e armazenar os dados em um Banco de Dados Postgres no AWS RDS (nuvem da Amazon).
  
### Arquivos
 São utilizados três arquivos para a execução desse projeto:
 - main.py - Contém a execução do programa em si (requisição dos dados da API, validação dos dados, carregamento dos dados no BD).
 - model.py - Conexão com o BD na Amazon RDS e criação da tabela.
 - config.py - Variáveis de configuração para conexão com o BD e parâmetros da API. 
