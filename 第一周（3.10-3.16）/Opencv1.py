import cv2
import numpy as np
img = cv2.imread('1.jpg')
cv2.imshow('1', img)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == 115:
    cv2.imwrite('a.bmp',img)
    cv2.destroyAllWindows()