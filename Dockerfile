# Usa un'immagine base ufficiale Python
FROM python:3.8-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia i file di requisiti prima per sfruttare la cache Docker layer
COPY requirements.txt .
COPY models models/

# Installa le dipendenze del progetto
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Copia il resto del codice sorgente dell'applicazione nel container
COPY . .

# Espone la porta su cui l'applicazione sarà disponibile
EXPOSE 8000

# Comando per eseguire l'applicazione
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
