import numpy as np
import cv2 as cv

# Incarcam videoclipul
video_path = "C:/Users/rdrah/Desktop/21.mp4"

# Atribuim variabilei cap videoclipul
cap = cv.VideoCapture(video_path)

# Specificam noua rezolutie dorita (640x480)
new_width, new_height = 600, 850

while True:
    ret, frame = cap.read()  # citeste variabila - videoul

    if not ret:
        print("Nu pot primii frameuri (video terminat?). Sfarsit...")
        break

    # Redimensionare la noua rezolutie
    frame = cv.resize(frame, (new_width, new_height))

    # Setează partea de sus a imaginii la culoarea neagră
    frame[:new_height//2, :] = [0, 0, 0]

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # setare in nuante de gri
    edges = cv.Canny(gray, 300, 400)  # creare contururi

    # Afisare frameuri origibal si final
    cv.imshow('Original Video', frame)
    cv.imshow('Edge Detection', edges)

    if cv.waitKey(1) == ord('q'):  # mod de incheiere al videourilor/programului
        break

cap.release()  # eliberare variabila
cv.destroyAllWindows()  # eliminare completa a tuturor ferestrelor deschise
