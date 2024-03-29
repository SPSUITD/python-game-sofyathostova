import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((511, 513)) # flags=pygame.NOFRAME
pygame.display.set_caption("Крутая игра")
icon = pygame.image.load('images/ikonka.png').convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.png').convert_alpha()
walk_left = [
    pygame.image.load('images/player_left/player_left1.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left2.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left3.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left4.png').convert_alpha(),
]

walk_right = [
    pygame.image.load('images/player_right/player_right1.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right2.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right3.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right4.png').convert_alpha(),
]


vrag = pygame.image.load('images/vrag.png').convert_alpha()

vrag_list_in_game = []
score = 0

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 330

is_jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
#bg_sound.play()

vrag_timer = pygame.USEREVENT + 1
pygame.time.set_timer(vrag_timer, 3500)

label = pygame.font.Font('fonts/Undertale-Battle-Font.ttf', 30)
lose_label = label.render('Вы проиграли!', True, (255, 255, 255))
restart_label = label.render('Играть заново', True, (139, 237, 100))
restart_label_rect = restart_label.get_rect(topleft=(60, 200))


bullets_left = 5
bullet = pygame.image.load('images/bullet.png').convert_alpha()
bullets = []
gameplay = True

running = True
while running:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 511, 0))
    score_label_play = label.render('Количество очков: ' + str(score), True, (0, 0, 0))
    score_label_lose = label.render('Количество очков: ' + str(score), True, (255, 255, 255))
    screen.blit(score_label_play, (10, 10))



    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        if vrag_list_in_game:
            for (i, el) in enumerate(vrag_list_in_game):
                screen.blit(vrag, el)
                el.x -= 10

                if el.x < player_x -100:
                    vrag_list_in_game.pop(0)
                    score += 1

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 200:
            player_x += player_speed


        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump =True
        else:
            if jump_count >= -7:
               if jump_count >0:
                   player_y -= (jump_count ** 2) / 2
               else:
                   player_y += (jump_count ** 2) / 2
               jump_count -= 1
            else:
                is_jump = False
                jump_count = 7

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -618:
            bg_x = 0

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 6

                if el.x > 550:
                    bullets.pop(i)

                if vrag_list_in_game:
                    for (index, vrag_el) in enumerate(vrag_list_in_game):
                        if el.colliderect(vrag_el):
                            vrag_list_in_game.pop(index)
                            bullets.pop(i)
                            score += 1
    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (60, 100))
        screen.blit(score_label_lose, (60, 150))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            vrag_list_in_game.clear()
            bullets.clear()
            score = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == vrag_timer:
            vrag_list_in_game.append(vrag.get_rect(topleft=(620, 430)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 110)))
            bullets_left -= 1
    clock.tick(10)