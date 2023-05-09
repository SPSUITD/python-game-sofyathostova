import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300)) # flags=pygame.NOFRAME
pygame.display.set_caption("Krutaya igra")
icon = pygame.image.load('images/ikonka.png')
pygame.display.set_icon(icon)

running = True

while running:

    screen.fill((67, 112, 75))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

