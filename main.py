from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.responses import FileResponse
from typing import List
import cv2
from Services.BlurringService import blur_image
import numpy as np
import tempfile
import os

app = FastAPI()

@app.post("/uploadimages")
async def upload_images(files: List[UploadFile]):
    saved_files = []
    for file in files:
        try:
            # Leggi il file dell'immagine
            image_data = await file.read()
            # Applica la funzione di sfocatura
            blurred_image = blur_image(image_data)  # Assumi che blur_image sia definita altrove

            # Salva l'immagine sfocata su disco
            temp_dir = tempfile.mkdtemp()
            temp_file = os.path.join(temp_dir, file.filename)
            is_success, buffer = cv2.imencode(".jpg", blurred_image)
            if not is_success:
                raise HTTPException(status_code=500, detail="Failed to process image")

            with open(temp_file, "wb") as f:
                f.write(buffer)

            saved_files.append(temp_file)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid image file: {str(e)}")

    if saved_files:
        return FileResponse(path=saved_files[-1], filename=saved_files[-1].split(os.sep)[-1], media_type='image/jpeg')
    else:
        raise HTTPException(status_code=500, detail="No files processed")
