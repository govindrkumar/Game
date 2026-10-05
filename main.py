import os
import pygame
import json
import random
import sys

pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

## Let me write height and width....
HEIGHT = 700
WIDTH = 1000

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FEED DOG")

## space image.....bolte
space_image_path = resource_path("assets/space.jpeg")
background = pygame.transform.scale(pygame.image.load(space_image_path), (WIDTH, HEIGHT))

dog_image_path = resource_path("assets/happy-dog.webp")
dog_image = pygame.transform.scale(
    pygame.image.load(dog_image_path),(80,80)
)

##----------
# So, here I will just create small variables....
##---------

dog_x = 80
dog_y = 100

## -------
# Cookie EATING---
##########

cookie_image_path = resource_path("assets/dog-cookie.png")
cookie = pygame.transform.scale(
    pygame.image.load(cookie_image_path),(40,40)
)

cookie_x = random.randint(0, WIDTH - 40)
cookie_y = random.randint(0, HEIGHT - 40)

## score logic
score = 0
font = pygame.font.Font(None, 30)
pygame.mixer.init() #initialised sound system
eat_sound = pygame.mixer.Sound(
    resource_path("assets/eat_dog.mp3")
)

## game run logic
running = True
while running:
    # window.blit tails this that go and display it....
    window.blit(background, (0,0))
    window.blit(dog_image, (dog_x, dog_y))

    window.blit(cookie, (cookie_x,cookie_y))
    


    pygame.draw.rect(window, (0,0,0), (800,20, 180,60))
    pygame.draw.rect(window, (255, 255, 255), (810, 30,160,40))

    
    text = font.render("FEED:", True, (0,0,0))

    window.blit(text, (820, 40))
    score_text = font.render(str(score), True, (0,0,0))
    window.blit(score_text, (920, 40))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and dog_x - 1 >= 0: 
        dog_x -= 1
    
    if keys[pygame.K_RIGHT] and dog_x + 1 <= WIDTH - 80:
        dog_x += 1
    
    if keys[pygame.K_UP] and dog_y - 1 >= 0:
        dog_y -= 1
    
    if keys[pygame.K_DOWN] and dog_y + 1 <= HEIGHT - 80:
        dog_y += 1
    
    dog_rect = dog_image.get_rect(topleft=(dog_x, dog_y))
    cookie_rect = cookie.get_rect(topleft=(cookie_x, cookie_y))
    if dog_rect.colliderect(cookie_rect):
        score += 1
        eat_sound.play()

        cookie_x = random.randint(0, WIDTH - 40)
        cookie_y = random.randint(0, HEIGHT - 40)

    
    pygame.display.flip()

    
pygame.quit()
