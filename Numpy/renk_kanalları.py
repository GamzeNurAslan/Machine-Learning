import cv2

image = cv2.imread("logo.png")

blue_channel1,green_channel1,red_channel1 = cv2.split(image)

cv2.imshow("Mavi kanal:", blue_channel1)
cv2.imshow("Kırmızı kanal:", red_channel1)
cv2.imshow("Yeşil kanal:", green_channel1)

cv2.waitKey(0)
cv2.destroyAllWindows()

modified_image = cv2.merge([blue_channel1,green_channel1,red_channel1])
cv2.imshow("Değiştirlmiş Kanal", modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
