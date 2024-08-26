# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos necessários para o contêiner
COPY requirements.txt .

# Instale as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define a variável de ambiente para Flask
ENV FLASK_APP=main.py

# Expõe a porta em que o Flask será executado
EXPOSE 5000

# Especifique o comando de inicialização
CMD ["python", "main.py"]
