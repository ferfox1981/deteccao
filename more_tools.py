import cv2 as cv

img = cv.imread("dados.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Imagem", gray) # exibe a imagem em uma janela
cv.waitKey(0) # aguarda até que uma tecla seja pressionada 

blur = cv.GaussianBlur(gray, (9,9), cv.BORDER_DEFAULT)

cv.imshow("Imagem", blur) # exibe a imagem em uma janela
cv.waitKey(0) # aguarda até que uma tecla seja pressionada

canny = cv.Canny(blur, 125, 175)
cv.imshow("Imagem", canny) # exibe a imagem em uma janela
cv.waitKey(0) # aguarda até que uma tecla seja pressionada

dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Imagem", dilated) # exibe a imagem em uma janela
cv.waitKey(0) # aguarda até que uma tecla seja pressionada

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
