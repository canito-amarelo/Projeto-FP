import pygame

pygame.init()

screen = pygame.display.set_mode((896, 704))
running = True
background = pygame.image.load("n1.png")
ze = pygame.image.load("Zé.png")

# Variáveis para troca de níveis
lvl1 = True
lvl2 = False
lvl3 = False
lvl4 = False
lvl5 = False

#Variáveis para o Zé
ze_x = 70
ze_y = 390
ze_vx = 0
ze_vy = 0


right_key = False
left_key = False
down_key = False

clock = pygame.time.Clock()


while running:
    up_key = False
    is_in_ladder = False
    # Variáveis para o salto
    if ze_y in [135, 265, 390, 520, 630]:
        is_in_floor = True
        
    

    # Variáveis para as escadas
    if lvl2:
        if 385 < ze_y < 519 and 365 < ze_x < 415:
            is_in_ladder = True


    # Eventos teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right_key = True
            if event.key == pygame.K_LEFT:
                left_key = True
            if event.key == pygame.K_UP:
                up_key = True
            if event.key == pygame.K_DOWN:
                down_key = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_key = False
            if event.key == pygame.K_LEFT:
                left_key = False
            if event.key == pygame.K_UP:
                up_key = False
            if event.key == pygame.K_DOWN:
                down_key = False

    # Lógica do jogo
    dt = clock.tick()

    # Velocidade horizontal
    if right_key:
        ze_vx = 0.15
    elif left_key:
        ze_vx = -0.15
    else: ze_vx = 0


    # Saltar
    if is_in_ladder and down_key:
        ze_vy = 0
        if ze_x < 390:
            ze_x = 390
        if ze_x > 410:
            ze_x = 410
    else:
        if is_in_floor and up_key:
            ze_vy = -3
            is_in_floor = False
        elif not is_in_floor:
            ze_vy = 0.01 * dt

    if down_key and is_in_ladder:
            if 386 < ze_y < 520:
                ze_y += 1
            else:
                down_key = False
            

    # Movimento horizontal do Zé
    
    ze_x += ze_vx*dt
    ze_vx = 0


    # Movimento vertical do Zé
    ze_y += int(ze_vy * dt)
    if 129 < ze_y < 134:
        is_in_floor = True
        ze_vy = 0
        ze_y = 135
    elif 259 < ze_y < 264:
        is_in_floor = True
        ze_vy = 0
        ze_y = 265
    elif 384 < ze_y < 389:
        is_in_floor = True
        ze_vy = 0
        ze_y = 390
    elif 514 < ze_y < 519:
        is_in_floor = True
        ze_vy = 0
        ze_y = 520
    elif 624 < ze_y < 629:
        is_in_floor = True
        ze_vy = 0
        ze_y = 630

    
    # Mecânica dos níveis
    # Nível 1
    if ze_x <= 40 and lvl1 == True:
        ze_x = 40
    
    # Nível 2
    if lvl1 == True and ze_x >= 880:
        background = pygame.image.load("n2.png")
        ze_x = 30
        lvl1 = False
        lvl2 = True
    if lvl2 == True:
        if ze_x <=10:
            background = pygame.image.load("n1.png")
            ze_x = 860
            lvl1 = True
            lvl2 = False


    # Nível 3
    if lvl2 == True and ze_x >= 880:
        background = pygame.image.load("n3.png")
        ze_x = 30
        lvl2 = False
        lvl3 = True
    if lvl3 == True:
        if ze_x <=10:
            background = pygame.image.load("n2.png")
            ze_x = 860
            lvl2 = True
            lvl3 = False

    if lvl3 == True and 150 < ze_y < 400:
        if ze_x >= 830:
            ze_x = 830

    # Nível 4
    if lvl3 == True and ze_x >= 880:
        background = pygame.image.load("n4.png")
        ze_x = 30
        lvl3 = False
        lvl4 = True
    if lvl4 == True:
        if ze_x <=10:
            background = pygame.image.load("n3.png")
            ze_x = 860
            lvl3 = True
            lvl4 = False

    if lvl4 == True and 265 < ze_y < 390:
        if ze_x <= 30:
            ze_x = 30

    # Nível 5
    if lvl4 == True and ze_x >= 880:
        background = pygame.image.load("n5.png")
        ze_x = 30
        lvl4 = False
        lvl5 = True
    if lvl5 == True:
        if ze_x <=10:
            background = pygame.image.load("n4.png")
            ze_x = 860
            lvl4 = True
            lvl5 = False
    if lvl5 == True and ze_x >= 830:
        ze_x = 830


    
    # Desenhar 
    screen.blit(background, (0,0))
    screen.blit(ze, (int(ze_x), int(ze_y)))
    
    pygame.display.flip()
    
pygame.quit()
