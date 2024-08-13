import random, time, os, pygame, sys
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
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
if money >= 1:
    bet = 1
else:
    bet = 0
########
#IMAGES#
muhbet_logo = pygame.transform.scale(pygame.image.load("img/MuhBet.png"), (2000, 1000))


orange_surface = pygame.transform.scale(pygame.image.load("img/orangerba.png"), (200, 100))

minus_surface = font.render("-", True, (255, 255, 255))
minus_button_rect = minus_surface.get_rect()
minus_button_rect.topleft = ((110, 50))

add_surface = font.render("+", True, (255, 255, 255))
add_button_rect = add_surface.get_rect()
add_button_rect.topleft = ((230, 50))



img_rocket_button_menu = pygame.transform.scale(pygame.image.load("img/Rocket.png"), (200, 100))
rocket_button_rect = img_rocket_button_menu.get_rect()
rocket_button_rect.topleft = ((width / 2) - (200 / 2), 300)

img_double_button_menu = pygame.transform.scale(pygame.image.load("img/Double.png"), (200, 100))
double_button_rect = img_double_button_menu.get_rect()
double_button_rect.topleft = ((width / 2) - (200 / 2), 400)

img_rocket = pygame.transform.scale(pygame.image.load("img/Cartoon_space_rocket.png"), (250, 250))
img_explosion = pygame.transform.scale(pygame.image.load("img/explosion.png"), (250, 250))

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
def default():
    global bet, money
    screen.fill((0, 0, 255))
    screen.blit(img_back, back_rect.topleft)
    screen.blit(img_cash, (20, 70))
    screen.blit(orange_surface, (80, 20))
    screen.blit(minus_surface, minus_button_rect.topleft)
    screen.blit(add_surface, add_button_rect.topleft)

    money_surface = font.render(f"{money:.2f}", True, (0, 255, 0))
    bet_surface = font.render(f"{bet}", True, (0, 0, 0))
    screen.blit(bet_surface, (170, 55))
    screen.blit(money_surface, (20, 120))


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MuhBet")
running = True
crashed = False
multi = 0.0
power = "off"
display = "menu"
cashout = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if minus_button_rect.collidepoint(mouse_pos):
                if power == "off" and bet > 1:
                    print("-1")
                    bet -= 1
                    print(bet)
            if add_button_rect.collidepoint(mouse_pos):
                if power == "off" and bet + 1 <= money:
                    print("+1")
                    bet += 1
                    print(bet)
            if back_rect.collidepoint(mouse_pos):
                if display == "menu":
                    running = False
                else:
                    display = "menu"
                    power = "off"
            if rocket_button_rect.collidepoint(mouse_pos):
                if display == "menu":
                    display = "rocket"
            if double_button_rect.collidepoint(mouse_pos):
                if display == "menu":
                    display = "double"
            if power == "on":
                if poweroff_rect.collidepoint(mouse_pos):
                    power = "off"
            elif power == "off":
                if poweron_rect.collidepoint(mouse_pos):
                    power = "on"

    if display == "menu":
        default()
        screen.blit(muhbet_logo, (width / 2 - 1000, -300))
        screen.blit(img_rocket_button_menu, rocket_button_rect.topleft)
        screen.blit(img_double_button_menu, double_button_rect.topleft)

    elif display == "rocket":
        default()
        screen.blit(img_rocket, (250, 100))

        if power == "off":
            random_float = False

            # print(cashout)
            if cashout == True:
                if bet > money:
                    bet = 0
                money += (bet * multi) - bet
                print("multi")
                print(multi)
                print("bet")
                print(bet)
                print(multi * bet)
                cashout = False

            multi = 0.0
            screen.blit(img_poweron, poweron_rect.topleft)
            clock.tick(60)
        elif power == "on":

            try:
                if random_float == False:
                    random_float = random.uniform(0, 10)
            except NameError:
                random_float = random.uniform(0, 10)
            elapsed_time = clock.tick(1000)
            multi += 0.002 * elapsed_time
            multi_surface = font.render(f"{multi:.1f}", True, (255, 255, 255))
            screen.blit(multi_surface, (width // 2 - 50, height // 2 + 50))
            # print(random_float)
            if multi > random_float:
                power = "off"
                random_float = False
                multi = 0.0
                screen.blit(img_explosion, (250, 100))
                if bet > money:
                    bet = 0
                pygame.display.flip()
                crashed = True
                ctimer = 0
            cashout = True
            screen.blit(img_poweroff, poweroff_rect.topleft)
        if crashed:
            ctimer += 1
            print(ctimer)
            screen.blit(img_rocket, (250, 100))
            screen.blit(img_explosion, (250, 100))
            multi_surface = font.render(f"{multi:.1f}", True, (255, 255, 255))
            if ctimer >= 100:
                crashed = False
            pygame.display.flip()
    elif display == "double":
        default()

    pygame.display.flip()
pygame.quit()
sys.exit()
