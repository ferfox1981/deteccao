import easyocr
import re

# Inicializa OCR em português
reader = easyocr.Reader(['pt'])

# Lê texto da imagem
resultado = reader.readtext("dados.png")

texto = " ".join([res[1] for res in resultado])
print("Texto extraído:", texto)

# Normaliza o texto para facilitar a detecção de CPFs
texto_normalizado = re.sub(r'\s+', '', texto)

# Procurar sequências de caracteres (ex: cpfs)
cpfs = re.findall(r'\d{3}\.\d{3}\.\d{3}-\d{2}', texto_normalizado)
print("CPFs encontrados:", cpfs)