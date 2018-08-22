import pygame, random
from src import *
pygame.init()

screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.fill((200,200,255))

	for i in game.sects:
		pygame.draw.rect(screen,(0,0,0),[random.randint(0,700),random.randint(0,500),30],4)

	pygame.display.update()