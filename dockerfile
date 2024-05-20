# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo da pasta local para o diretório de trabalho no container
COPY . .

# Exponha a porta que o Tornado usará
EXPOSE 8000

# Defina o comando para rodar a aplicação
CMD ["python", "main.py"]

