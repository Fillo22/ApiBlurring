import cv2
import numpy as np
from pathlib import Path


_MODELS_DIR = Path(__file__).resolve().parent.parent / "models"
_FACE_CASCADE = cv2.CascadeClassifier(str(_MODELS_DIR / "haarcascade_frontalface_default.xml"))
_PLATE_CASCADE = cv2.CascadeClassifier(str(_MODELS_DIR / "haarcascade_russian_plate_number.xml"))


def _validate_classifiers():
    if _FACE_CASCADE.empty() or _PLATE_CASCADE.empty():
        raise RuntimeError(f"Unable to load cascade files from {_MODELS_DIR}")


def blur_image(image_input):
    _validate_classifiers()

    # Converti l'input binario in un array numpy
    nparr = np.frombuffer(image_input, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Unable to decode image from input bytes")

    # Converti l'immagine in scala di grigi per il rilevamento
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Rilevamento di volti e targhe
    faces = _FACE_CASCADE.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    plates = _PLATE_CASCADE.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Applica sfocatura gaussiana ai volti rilevati
    for (x, y, w, h) in faces:
        roi = image[y:y + h, x:x + w]
        blurred_roi = cv2.GaussianBlur(roi, (23, 23), 0)
        image[y:y + h, x:x + w] = blurred_roi

    # Applica sfocatura gaussiana alle targhe rilevate
    for (x, y, w, h) in plates:
        roi = image[y:y + h, x:x + w]
        blurred_roi = cv2.GaussianBlur(roi, (23, 23), 0)
        image[y:y + h, x:x + w] = blurred_roi

    return image
