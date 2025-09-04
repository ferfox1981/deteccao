import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("VELHA.png") # lê uma imagem e retorna como uma matriz de pixels

cv.imshow("Imagem", img) # exibe a imagem em uma janela
cv.waitKey(0) # aguarda até que uma tecla seja pressionada (se for colocado zero), caso contrário, aguarda indefinidamente
cv.destroyAllWindows() # fecha todas as janelas abertas


# Aprendendo o resize e rescale uma imagem, isso 

img_resized = rescaleFrame(img, scale=0.2)
cv.imshow("Imagem Redimensionada", img_resized)
cv.waitKey(0)
cv.destroyAllWindows()

