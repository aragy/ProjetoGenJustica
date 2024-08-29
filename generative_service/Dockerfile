
FROM custom_ollama_base

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
#RUN ollama serve

COPY app/ ./app/


EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["sh", "-c", "ollama serve & uvicorn app.main:app --host 0.0.0.0 --port 8000"]