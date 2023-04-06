# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos do projeto
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do projeto
COPY app.py .

# Exponha a porta em que a aplicação será executada
EXPOSE 5000

# Inicie a aplicação
CMD ["python", "app.py"]
