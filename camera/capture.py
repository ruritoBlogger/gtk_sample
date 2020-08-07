import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
     
    if frame is not None:
        cv2.imshow("title", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
