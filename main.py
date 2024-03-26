import numpy as np
import cv2 as cv

video_path = "video.mp4"

cap = cv.VideoCapture(video_path)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Nu pot primii frameuri (video terminat?). Sfarsit...")
        break

    # Convertim frame-ul în tonuri de gri
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detectăm marginile pentru detecția benzilor
    edges = cv.Canny(gray, 100, 200)

    # Definim regiunea de interes pentru detecția benzilor
    height, width = edges.shape
    region_of_interest_vertices = [
        (0, height),
        (width * 0.4, height * 0.6),
        (width * 0.6, height * 0.6),
        (width, height),
    ]
    mask = np.zeros_like(edges)
    cv.fillPoly(mask, np.array([region_of_interest_vertices], np.int32), 255)
    masked_edges = cv.bitwise_and(edges, mask)

    # Filtrăm frame-ul original cu un background negru
    filtered_frame = np.zeros_like(frame)
    filtered_frame[mask != 0] = frame[mask != 0]

    # Adăugăm un layout verde doar pe banda de circulație
    lane_layout = np.zeros_like(frame)
    lane_layout[:, :, 1] = 255  # Setăm canalul verde la maxim pentru layout-ul benzii de circulație

    # Combinăm frame-ul filtrat cu layout-ul benzii de circulație
    frame_with_lane_layout = cv.addWeighted(filtered_frame, 1, lane_layout, 0.5, 0)

    # Afișăm linii albe pe șosea
    frame_with_lane_layout[masked_edges != 0] = [255, 255, 255]

    # Afișăm textul pe frame
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame_with_lane_layout, 'Banda de circulatie', (50, 50), font, 1, (0, 0, 255), 2, cv.LINE_AA)

    # Afișăm frame-ul original și frame-ul cu edge detection
    cv.imshow('Original Video', frame)
    cv.imshow('Filtered Video', frame_with_lane_layout)

    # Așteptăm 30 de milisecunde între fiecare frame și verificăm dacă a fost apăsată tasta 'q' pentru a încheia bucla
    if cv.waitKey(30) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
