import cv2


vid = cv2.VideoCapture(0)
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    flag, fream = vid.read()
    if flag:
        gray = cv2.cvtColor(fream,cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(fream, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.waitKey(1)
        cv2.imshow("result", fream)
        cv2.waitKey(1)

vid.release()
cv2.destroyAllWindows()

