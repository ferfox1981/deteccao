import cv2

# Carregar imagens
img_ref = cv2.imread("NOVA.png", cv2.IMREAD_GRAYSCALE)   # imagem guardada (referência)
img_new = cv2.imread("VELHA.png", cv2.IMREAD_GRAYSCALE) # imagem nova (do software)

# Inicializar ORB. O ORB encontra pontos característicos nas duas imagens.
orb = cv2.ORB_create()

# Detectar keypoints e descritores
kp1, des1 = orb.detectAndCompute(img_ref, None)
kp2, des2 = orb.detectAndCompute(img_new, None)

# Comparar descritores com o matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Ordenar pelo melhor "score"
matches = sorted(matches, key=lambda x: x.distance)

# Calcular média da distância dos melhores matches
good_matches = matches[:30]  # pega os 30 melhores
avg_dist = sum([m.distance for m in good_matches]) / len(good_matches)

print(f"Média da distância: {avg_dist:.2f}")

# Definir limiar de semelhança (ajustável)
if avg_dist < 50:
    print("✅ As imagens são semelhantes!")
else:
    print("❌ As imagens são diferentes.")

# Visualizar correspondências (opcional)
resultado = cv2.drawMatches(img_ref, kp1, img_new, kp2, good_matches, None, flags=2)
cv2.imshow("Matches", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
