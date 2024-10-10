# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
import pygame
import time

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo MP3 duplicando as barras invertidas(\\) ou substituindo por barras normais(/)
arquivo_mp3 = 'C:\\Users\\Master\\Documents\\GitHub\\CursoEmVideo_Python\\Mundo01\\lobo-pidao.mp3'
pygame.mixer.music.load(arquivo_mp3)

# Reproduzir o arquivo MP3
pygame.mixer.music.play()

# Esperar até que a reprodução termine
while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Reprodução concluída.")
