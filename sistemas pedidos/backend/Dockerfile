# Usa a imagem oficial do Python
FROM python:3.12

# Define o diretório de trabalho no container
WORKDIR /app

# Copia apenas requirements.txt primeiro (melhora cache)
COPY requirements.txt /app/

# Instala as dependências antes de copiar o restante do código
RUN pip install --upgrade pip
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Copia os arquivos do projeto para o container
COPY . /app/

# Expõe a porta do Django
EXPOSE 8000

# Comando padrão para rodar o servidor
CMD ["sh", "-c", "ls -la /app/hotelproject && python hotelproject/manage.py migrate && python hotelproject/manage.py runserver 0.0.0.0:8000"]
