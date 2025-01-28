# Use a imagem oficial do Python
FROM python:3.10-slim

# Configurar o diretório de trabalho
WORKDIR /app

# Instalar dependências de compilação
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de dependências
COPY requirements.txt /app/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . /app/

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando padrão ao iniciar o container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
