import cv2
import numpy as np


def blur_image(image_input):
    # Converti l'input binario in un array numpy
    nparr = np.frombuffer(image_input, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Carica i classificatori preaddestrati per il riconoscimento di volti e targhe
    face_cascade = cv2.CascadeClassifier('/app/models/haarcascade_frontalface_default.xml')
    plate_cascade = cv2.CascadeClassifier('/app/models/haarcascade_russian_plate_number.xml')

    # Converti l'immagine in scala di grigi per il rilevamento
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Rilevamento di volti e targhe
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

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
