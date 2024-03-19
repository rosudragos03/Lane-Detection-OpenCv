import numpy as np
import cv2 as cv

# Incarcam videoclipul
video_path = "C:/Users/rdrah/Desktop/Lane-Detection-OpenCv/Recording/video_R_D.mp4"

# Atribuim variabilei cap videoclipul
cap = cv.VideoCapture(video_path)

# Specificam noua rezolutie dorita (640x480)
new_width, new_height = 600, 850

while True:
    ret, frame = cap.read()  # citeste variabila - videoul

    if not ret:
        print("Nu pot primii frameuri (video terminat?). Sfarsit...")
        break

    # noua rezolutie
    frame = cv.resize(frame, (new_width, new_height))

    # Setează partea de sus a imaginii la culoarea neagră
    frame[:new_height//2, :] = [0, 0, 0]

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # imagine alb-negru

    edges = cv.Canny(gray, 300, 400) # creare contururi
    # detectarea linilor albe
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=50)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2) #identificarea linilor albe

    cv.imshow('Edge Detection', edges)
    cv.imshow('Original Video', frame)  # afisare video result

    if cv.waitKey(1) == ord('q'):  # mod de încheiere al videourilor/programului
        break

cap.release()  # eliberare variabila
cv.destroyAllWindows()  # eliminare completa a tuturor ferestrelor deschise
