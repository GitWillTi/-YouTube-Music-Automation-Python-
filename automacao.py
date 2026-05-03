import pyautogui as pa
import time

# Configurações
pa.PAUSE = 1
pa.FAILSAFE = True

print("🎵")

# 1. Abre o Firefox
pa.press('win')
time.sleep(0.5)
pa.write('firefox')
pa.press('enter')
time.sleep(5)

# 2. Vai para o YouTube
pa.hotkey('ctrl', 'l')
pa.write('https://www.youtube.com')
pa.press('enter')
print("📺 Carregando YouTube...")
time.sleep(2)

# 3. CLICA NA BARRA DE PESQUISA
pa.click(x=893, y=132)
print("🔍 Clicou na barra de pesquisa...")
time.sleep(1)

# 4. Digita a música
pa.write('ANAVITÓRIA, Jorge & Mateus - Geleira do tempo', interval=0.3)
pa.press('enter')
print("📋 Pesquisando...")
time.sleep(6)

# 5. CLICA NO SEGUNDO VÍDEO (evitando anúncio)
pa.click(x=769, y=716)
print("▶️ Clicou no SEGUNDO vídeo...")
time.sleep(5)

# 6. Tela cheia
pa.press('f')
print("🎸")