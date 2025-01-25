# Documentação PDF Scanner

## Instalação

1. Faça um clone do repositorio atual
2. Após feito o clone abra a pasta clonada "alex-projeto" no CMD
3. Com a pasta aberta crie um ven com o seguinte comando

```bash
python -m venv venv
```

Caso não dé certo utilize o seguinte comando

```bash
python3 -m venv venv
```

4. Com o venv criado podemos executa-lo utilizando o seguinte comando caso esteja no Windows:

```bash
venv/Scripts/activate
```

Ou no Linux:

```bash
source venv/bin/activate
```

5. Com o ambiente virtual ativado podemos seguir com as instalações das dependencias com o seguinte comando

```bash
pip install -r requirements.txt
```

6. Após instalar as dependencias podemos executar o projeto

## Execução

1. Com as dependecias instaladas e o venv criado podemos executar o projeto, para isso primeiros podemos abrir o VsCode utilizando o seguinte comando

```bash
code .
```

2. Com o VsCode aberto, podemos instalar a extensão do python na loja - Extensão: Python / Microsoft

3. Com a extensão instalada podemos voltar a pasta e abrir o script app.py

4. Com o Script aberto podemos abertar o atalho F5 e então executar o arquivo app.py

5. Caso seja a primeira vez executando um arquivo com a extensão ele exibira algumas opções podemos escolher a primeira opção - Arquivo Python - e ele será executado

6. Agora já dentro da aplicação teremos duas opções

   a. Imagem para Documento:
   Nesta opção teremos a funcionalidade de scanner imagens e então converter para um .docx editavel

   b. PDF para Documento:
   Já nesta opção teremos a funcionalidade de scanner um arquivo PDF e então converte-lo para um .docx editavel

7. Após selecionar uma das opções podemos então anexar o arquivo desejado e converte-lo

8. Após convertido o arquivo .docx será baixado automaticamente e então podemos abri-lo para confirmar o conteudo extraido do documento que anexamos
