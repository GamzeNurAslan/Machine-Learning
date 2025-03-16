import cv2
import numpy as np
#OpenCV'nin renk kodu BGR

image = np.zeros((500,500,3), dtype="uint8")

cv2.line(image,(50,50),(450,50), (0,255,0), 3)
cv2.rectangle(image, (100,100), (400,300), (255,0,0), -1)
cv2.rectangle(image, (100,100), (400,300), (255,0,0), 2)
cv2.circle(image, (250,250),50,(0,0,255),2)

points = np.array([[200,100],[300,250],[100,200]])

cv2.polylines(image, [points],isClosed=True, color=(255,255,0), thickness=3)

cv2.putText(image, "OPENCV ile Görüntü İşleme",(50,450),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,0))

cv2.imshow("Siyah Plan", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
