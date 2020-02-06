import cv2

cascade_file = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('abc.jpg',1)

faces = cascade_file.detectMultiScale(img,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,255,0),2)


cv2.imshow('RESULT',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

