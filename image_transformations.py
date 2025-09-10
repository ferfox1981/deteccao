import cv2 as cv
import numpy as np


# translation, resizing, rotation, flipping, cropping

img = cv.imread("dados.png")

# translation - shifting the image in x and y direction
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# +x --> right
# +y --> down
translated = translate(img, -100, 100)
cv.imshow("Translated", translated)
cv.waitKey(0)

# Rotation
# podemos rotar uma imagem em torno de um ponto especifico, normalmente o centro da imagem
def rotate(img, angle, rotPoint=None):
     (height, width) = img.shape[:2]

     if rotPoint is None:
         rotPoint = (width//2, height//2) # a divisao inteira

     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
     dimensions = (width, height)

     return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)
cv.waitKey(0)

# Flipping
flip = cv.flip(img, 1) # 0 vertical, 1 horizontal, -1 ambos
cv.imshow("Flip", flip)
cv.waitKey(0)