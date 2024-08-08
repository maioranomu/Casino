import random, time, os, pygame, sys
pygame.init()
width = 600
height = 600

money, file = float(10), "import.txt"
with open(file, "r") as f:
    try:
        money = float(f.read())
    except ValueError:
        money = float(50)
        with open(file, "w") as f:
            f.write(str(money))

########
#IMAGES#
muhbet_logo = pygame.transform.scale(pygame.image.load("img/MuhBet.png"), (2000, 1000))

img_rocket_button_menu = pygame.transform.scale(pygame.image.load("img/Rocket.png"), (200, 100))
rocket_button_rect = img_rocket_button_menu.get_rect()
rocket_button_rect.topleft = ((width / 2) - (200 / 2), 300)

img_double_button_menu = pygame.transform.scale(pygame.image.load("img/Double.png"), (200, 100))
double_button_rect = img_double_button_menu.get_rect()
double_button_rect.topleft = ((width / 2) - (200 / 2), 400)

img_rocket = pygame.transform.scale(pygame.image.load("img/Cartoon_space_rocket.png"), (250, 250))

img_back = pygame.transform.scale(pygame.image.load("img/back.png"), (50, 50))
back_rect = img_back.get_rect()
back_rect.topleft = (20, 20)

img_cash = pygame.transform.scale(pygame.image.load("img/dollars.png"), (50, 50))

img_closex = pygame.transform.scale(pygame.image.load("img/closex.png"), (50, 50))

img_poweron = pygame.transform.scale(pygame.image.load("img/power.png"), (100, 100))
poweron_rect = img_poweron.get_rect()
poweron_rect.topleft = (width / 2 - 25, 450)

img_poweroff = pygame.transform.scale(pygame.image.load("img/power-off.png"), (100, 100))
poweroff_rect = img_poweroff.get_rect()
poweroff_rect.topleft = (width / 2 - 25, 450)
########

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MuhBet")
running = True

power = "on"
display = "menu"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if back_rect.collidepoint(mouse_pos):
                if display == "menu":
                    running = False
                else:
                    display = "menu"
                    power = "off"
            if rocket_button_rect.collidepoint(mouse_pos):
                display = "rocket"
            if double_button_rect.collidepoint(mouse_pos):
                display = "double"
            if power == "on":
                if poweroff_rect.collidepoint(mouse_pos):
                    power = "off"
                    print("off")

            elif power == "off":
                if poweron_rect.collidepoint(mouse_pos):
                    power = "on"
                    print("on")


    if display == "menu":
        screen.fill((0, 0, 255))
        screen.blit(muhbet_logo, (width / 2 - 1000, -300))
        screen.blit(img_back, back_rect.topleft)
        screen.blit(img_cash, (20, 70))
        screen.blit(img_rocket_button_menu, rocket_button_rect.topleft)
        screen.blit(img_double_button_menu, double_button_rect.topleft)

    elif display == "rocket":
        screen.fill((0, 0, 255))
        screen.blit(img_back, back_rect.topleft)
        screen.blit(img_cash, (20, 70))
        screen.blit(img_rocket, (250, 100))
        if power == "off":
            screen.blit(img_poweron, poweron_rect.topleft)
        elif power == "on":
            screen.blit(img_poweroff, poweroff_rect.topleft)
        pygame.display.flip()

    elif display == "double":
        print("double")
        screen.fill((0, 0, 255))
        screen.blit(img_back, back_rect.topleft)
        screen.blit(img_cash, (20, 70))

    pygame.display.flip()
pygame.quit()
sys.exit()