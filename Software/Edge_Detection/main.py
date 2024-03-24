import numpy as np
import cv2 as cv

# Incarcam videoclipul
video_path = "C:/Users/rdrah/Desktop/Lane-Detection-OpenCv/Recording/video_R_D.mp4"

# Atribuim variabilei cap videoclipul
cap = cv.VideoCapture(video_path)

# Specificam noua rezolutie dorita
new_width, new_height = 600, 850

paused = False  # verifica daca videoclipul este in pauza sau nu
frame_index = 0  # indexul curent al frame-ului

while True:
    if not paused or cv.waitKey(0) == ord('n'):
        ret, frame = cap.read()  # citeste variabila - videoul

        if not ret:
            print("Nu pot primii frameuri (video terminat?). Sfarsit...")
            break

        # noua rezolutie
        frame = cv.resize(frame, (new_width, new_height))

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # imagine alb-negru

        edges = cv.Canny(gray, 300, 400)  # creare contururi

        # Creăm o mască pentru a aplica filtrul doar pe partea de jos a imaginii
        mask = np.zeros_like(edges)
        mask[new_height // 2 + 50:, :] = 255  # Tăiem mai jos de jumătatea imaginii

        # Aplicăm filtrul de contur doar pe partea de jos a imaginii folosind mască
        edges_masked = cv.bitwise_and(edges, mask)

        # Detectează contururile
        contours, _ = cv.findContours(edges_masked, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Desenează contururile detectate pe imaginea originală
        cv.drawContours(frame, contours, -1, (0, 0, 255), 2)

        cv.imshow('Edge Detection', edges_masked)
        cv.imshow('Original Video', frame)  # afisare video result

        key = cv.waitKey(30)
        if key == ord('q'):  # mod de încheiere al videourilor/programului
            break
        elif key == ord('p'):  # Pauză/oprire videoclip când se apasă 'p'
            paused = not paused
        elif key == ord('n'):  # Trecere la următorul cadru când se apasă 'n'
            frame_index += 1
            cap.set(cv.CAP_PROP_POS_FRAMES, frame_index)

    else:
        key = cv.waitKey(0)  # Așteaptă tasta apăsată
        if key == ord('q'):  # mod de încheiere al videourilor/programului
            break
        elif key == ord('p'):  # Continuă redarea videoclipului când se apasă 'p'
            paused = not paused

cap.release()  # eliberare variabila
cv.destroyAllWindows()  # eliminare completa a tuturor ferestrelor deschise 
