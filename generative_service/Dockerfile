# Use a imagem customizada como base
FROM custom_ollama_base

# Definir diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências e instalar
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
#RUN ollama serve

# Copiar o código da aplicação
COPY app/ ./app/

# Expor a porta necessária
EXPOSE 8000

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["sh", "-c", "ollama serve & uvicorn app.main:app --host 0.0.0.0 --port 8000"]