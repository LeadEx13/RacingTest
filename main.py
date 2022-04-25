import pygame
pygame.init()
import random

screen = pygame.display.set_mode((798, 600))
pygame.display.set_caption('Crash Test')

def gameloop():

    bg = pygame.image.load('cars/bg.png')

    maincar = pygame.image.load('cars\car.png')
    maincarX = 350
    maincarY = 495
    maincarX_change = 0
    maincarY_change = 0

    car1 = pygame.image.load('cars\car1.jpeg')
    car1X = random.randint(178, 490)
    car1Y = 100

    car2 = pygame.image.load('cars\car2.png')
    car2X = random.randint(178, 490)
    car2Y = 100

    car3 = pygame.image.load('cars\car3.png')
    car3X = random.randint(178, 490)
    car3Y = 100

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    maincarX_change += 5

                if event.key == pygame.K_LEFT:
                    maincarX_change -= 5

                if event.key == pygame.K_UP:
                    maincarY_change -= 5

                if event.key == pygame.K_DOWN:
                    maincarY_change += 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    maincarX_change = 0

                if event.key == pygame.K_LEFT:
                    maincarX_change = 0

                if event.key == pygame.K_UP:
                    maincarY_change = 0

                if event.key == pygame.K_DOWN:
                    maincarY_change = 0

        if maincarX < 178:
            maincarX = 178
        if maincarX > 490:
            maincarX = 490

        if maincarY < 0:
            maincarY = 0
        if maincarY > 495:
            maincarY = 495

        screen.fill((0, 0, 0))

        screen.blit(bg, (0, 0))

        screen.blit(maincar, (maincarX, maincarY))

        screen.blit(car1, (car1X, car1Y))
        screen.blit(car2, (car2X, car2Y))
        screen.blit(car3, (car3X, car3Y))

        maincarX += maincarX_change
        maincarY += maincarY_change

        car1Y += 10
        car2Y += 10
        car3Y += 10

        if car1Y > 670:
            car1Y = -100
        if car2Y > 670:
            car2Y = -150
        if car3Y > 670:
            car3Y = -200

        pygame.display.update()

gameloop()