import easyocr
import re
import cv2
import numpy as np

# Inicializa OCR em português
reader = easyocr.Reader(['pt'])

# Lê a imagem
image_path = "dados.png"
image = cv2.imread(image_path)

# Detecta texto e obtém bounding boxes
resultado = reader.readtext(image_path, detail=1)

cpfs = []

for res in resultado:
    bbox, text, conf = res
    # Calcular o ângulo do texto usando os pontos do bounding box
    (tl, tr, br, bl) = bbox
    dx = tr[0] - tl[0]
    dy = tr[1] - tl[1]
    angle = np.degrees(np.arctan2(dy, dx))

    # Deskew se o ângulo for significativo (por exemplo, > 5 graus)
    if abs(angle) > 5:
        # Crop da região do texto
        pts = np.array(bbox, dtype="float32")
        rect = cv2.boundingRect(pts)
        x, y, w, h = rect
        cropped = image[y:y+h, x:x+w]

        # Rotaciona a região
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(cropped, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

        # OCR na região rotacionada
        region_result = reader.readtext(rotated)
        region_text = " ".join([r[1] for r in region_result])
    else:
        region_text = text

    # Normaliza e procura CPF
    texto_normalizado = re.sub(r'\s+', '', region_text)
    cpfs_encontrados = re.findall(r'\d{3}\.\d{3}\.\d{3}-\d{2}', texto_normalizado)
    cpfs.extend(cpfs_encontrados)

print("CPFs encontrados:", cpfs)