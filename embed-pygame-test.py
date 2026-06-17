import pygame
import requests
import sys
from io import BytesIO
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))

response = requests.get('https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XsnXwtmkJjSU91dh8bj35VTqVBP4io_fr3EVvKD6MKU_cKPKXWHFxLkls7FsSnDqwUl_sWTczoqheHifbwMmD5F1RvlK7Ec_KL6Q_A')

img = pygame.image.load(BytesIO(response.content))

while True:  # Game Loop


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(img, (0, 0))
    pygame.display.update()
    response = requests.get(
        'https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XsnXwtmkJjSU91dh8bj35VTqVBP4io_frHcVuPaoafU1JqiVWWSVkux15OQ8Giiylk0k5mvTnIqpd3PCaQIhWMYkE_lK7EcNeCKW-w')
    img = pygame.image.load(BytesIO(response.content))
    screen.blit(img, (0, 0))
    pygame.display.update()