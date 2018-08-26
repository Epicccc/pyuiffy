import pygame, random
from src import *

def text(text,size,font, color=[255,255,255]):
    myfont = pygame.font.SysFont(font, size)
    return myfont.render(text, False, (color[0],color[1],color[2]))
def mousein(x,y,w,h):
    if mx >= x and my >= y and mx <= x+w and my <= y+h: return True
    else: return False

pygame.init()

screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	mx,my = pygame.mouse.get_pos()
	left,mid,right = pygame.mouse.get_pressed()

	screen.fill((200,200,255))

	for i in sections:
		if mousein(i.x,i.y,40,20) and left == 1:
			i.x,i.y = [mx-10,my-10]
		pygame.draw.rect(screen,(0,0,0),[i.x,i.y,40,20],4)
		for j in i.options:
			for k in sections:
				if k.nm == j[0]:
					pygame.draw.line(screen,(0,0,100),(i.x,i.y),(k.x,k.y))
		screen.blit(text(i.nm,10,"Arial"),(i.x+5,i.y+4))
	for i in passages:
		if mousein(i.x,i.y,40,20) and left == 1:
			i.x,i.y = [mx-10,my-10]
		pygame.draw.rect(screen,(0,0,0),[i.x,i.y,40,20],4)
		for j in i.options:
			for k in passages:
				if k.nm == j[0]:
					pygame.draw.line(screen,(0,0,100),(i.x,i.y),(k.x,k.y))
		screen.blit(text(i.nm,10,"Arial"),(i.x+5,i.y+4))

	pygame.display.update()