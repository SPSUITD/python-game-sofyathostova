import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300)) # flags=pygame.NOFRAME
pygame.display.set_caption("Krutaya igra")
icon = pygame.image.load('images/ikonka.png')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 170))
square.fill('Blue')

myfont = pygame.font.Font('fonts/Undertale-Battle-Font.ttf', 40)
text_surface = myfont.render('Привет! Это игра.', True, 'White')
player = pygame.image.load('images/ikonka.png')
running = True
while running:

    pygame.draw.circle(screen, 'Red', (10, 7), 5)
    screen.blit(square, (10, 0))
    screen.blit(text_surface, (300, 100))
    screen.blit(player, (20, 5))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()