import cv2
import numpy as np


def blur_image(image_input):
    image = cv2.imread(image_input)
    face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
    plate_cascade = cv2.CascadeClassifier('models/haarcascade_russian_plate_number.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 10)

    for (x, y, w, h) in plates:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 10)

    # Apply Gaussian blurring to the detected faces and license plates
    for (x, y, w, h) in faces:
        roi = image[y:y + h, x:x + w]
        blurred_roi = cv2.GaussianBlur(roi, (255, 255), 0)
        image[y:y + h, x:x + w] = blurred_roi

    for (x, y, w, h) in plates:
        roi = image[y:y + h, x:x + w]
        blurred_roi = cv2.GaussianBlur(roi, (255, 255), 0)
        image[y:y + h, x:x + w] = blurred_roi

    return image


class BlurringService:
    pass
