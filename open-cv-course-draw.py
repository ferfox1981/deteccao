import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8") # uma imagem em branco. O 3 significa que a imagem tem 3 canais (RGB)

#img = cv.imread("VELHA.png") # lê uma imagem e retorna como uma matriz de pixels

blank[:] = (0, 255, 0)


cv.putText(blank, "Olá Mundo!", (100, 250), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2) # adiciona texto na imagem. Parâmetros: imagem, texto, posição (x,y), fonte, escala, cor (BGR), espessura

cv.imshow("Imagem", blank) # exibe a imagem em uma janela
cv.waitKey(0) # aguarda até que uma tecla seja pressionada (se for colocado zero), caso contrário, aguarda indefinidamente



