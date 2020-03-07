import cv2
import sys

#read image
image = cv2.imread("C:/Users/Asus/Desktop/abc.jpg")

output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

output = cv2.GaussianBlur(output, (3,3), 0)

output = cv2.Laplacian(output, -1, ksize=3)

output = 255 - output

ret, output = cv2.threshold(output, 150, 255, cv2.THRESH_BINARY)

cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)

cv2.imshow("image", image)
cv2.imshow("pencilsketch", output)

cv2.waitKey(0)

cv2.destroyAllWindows()
