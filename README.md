# API para previsão de risco de crédito

Esta API tem a finaliade de gera dados falsos para análise e previsão de risco de crédito ao consumidor, utilizando informações demográficas, financeiras e comportamentais.

## Funcionalidades
- Geração de dados demográficos como idade, gênero, estado civil e dependentes.
- Informações financeiras como renda mensal, histórico de crédito, patrimônio líquido e limite de crédito.
- Comportamento de pagamento como histórico de pagamento e utilização de crédito.
- Detalhes de empréstimo, como montante, taxa de juros e prazo.
- Dados geográficos e relacionados ao emprego.
- Suporte para geração de endereços brasileiros.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Execução

Para rodar a API localmente:

1. Inicie o servidor Flask:

   ```bash
   python app.py
   ```

2. Acesse a API em `http://127.0.0.1:5000/generate-data` no seu navegador ou ferramenta como o Postman.

## Exemplos de Uso

Utilize o Postman ou outro cliente HTTP para enviar requisições `GET` à rota `/generate-data`. A API retornará um JSON com os dados gerados.

## Contribuições

Pull requests são bem-vindos. Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de alterar.
