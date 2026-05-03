import pyautogui as pa
import time

print("Posicione o mouse sobre a BARRA DE PESQUISA do YouTube")
print("(a barra principal no topo da página)")
print("Você tem 5 segundos...")
time.sleep(5)
x, y = pa.position()
print(f"Coordenadas da BARRA DE PESQUISA: x={x}, y={y}")