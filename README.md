# API di Sfocatura Immagini

## Descrizione
L'API di Sfocatura Immagini è un servizio web sviluppato con FastAPI che permette agli utenti di caricare immagini e ricevere in cambio versioni sfocate delle stesse. È particolarmente utile per oscurare i volti o le targhe nelle immagini per questioni di privacy.

## Caratteristiche
- Rilevamento di volti e targhe nelle immagini.
- Sfocatura delle aree rilevate per proteggere la privacy.
- Semplice da usare con una singola chiamata API.

## Installazione
Per utilizzare l'API di Sfocatura Immagini, è possibile eseguire l'applicazione localmente o tramite Docker.

### Requisiti
- Python 3.8+
- Docker (opzionale per l'uso con Docker)

### Setup Locale
1. Clona il repository:
    ```bash
    git clone https://github.com/fillo22/api-blurring.git
    cd api-blurring
    ```

2. Crea e attiva un ambiente virtuale (opzionale ma raccomandato):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Su Windows usa `venv\Scripts\activate`
    ```

3. Installa le dipendenze:
    ```bash
    pip install -r requirements.txt
    ```

4. Avvia l'applicazione:
    ```bash
    uvicorn main:app --reload
    ```

L'applicazione sarà accessibile all'indirizzo: `http://localhost:8000`

### Uso con Docker
1. Costruisci l'immagine Docker:
    ```bash
    docker build -t api-blurring .
    ```

2. Avvia il container:
    ```bash
    docker run -d --name api-blurring -p 8000:8000 api-blurring
    ```

L'applicazione sarà accessibile all'indirizzo: `http://localhost:8000`

## Uso
Per sfocare le immagini, invia una richiesta POST all'endpoint `/uploadimages` con l'immagine da sfocare.

Esempio con `curl`:
```bash
curl -X POST "http://localhost:8000/uploadimages" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "files=@path_to_image.jpg"
