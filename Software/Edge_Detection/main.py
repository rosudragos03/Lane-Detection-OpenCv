import numpy as np
import cv2 as cv

# Incarcam videoclipul
video_path = "video.mp4"

# atribuim variabilei cap videoclipul
cap = cv.VideoCapture(video_path)

while True:
    ret, frame = cap.read() # citeste variabila - videoul

    if not ret:
        print("Nu pot primii frameuri (video terminat?). Sfarsit...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # setare in nuante de gri
    edges = cv.Canny(gray, 100, 200) # creare contururi

    # Afisare frameuri origibal si final
    cv.imshow('Original Video', frame)
    cv.imshow('Edge Detection', edges)

    if cv.waitKey(1) == ord('q'): # mod de incheiere al videourilor/programului
        break

cap.release() # eliberare variabila
cv.destroyAllWindows() # eliminare completa a tuturor ferestrelor deschise