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
        money = float(10)
        with open(file, "w") as f:
            f.write(str(money))
if money >= 1:
    bet = 1
else:
    bet = 0
    money = float(10)
    with open(file, "w") as f:
        f.write(str(money))
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
poweron_rect.topleft = (width / 2 - 50, 470)

img_poweroff = pygame.transform.scale(pygame.image.load("img/power-off.png"), (100, 100))
poweroff_rect = img_poweroff.get_rect()
poweroff_rect.topleft = (width / 2 - 50, 470)

img_blue_square = pygame.transform.scale(pygame.image.load("img/blue_square.png"), (100, 400))
img_white_pointer = pygame.transform.scale(pygame.image.load("img/white_pointer.png"), (10, 150))

img_white_square = pygame.transform.scale(pygame.image.load("img/white_square.png"), (155 / 2, 155 / 2))
action_white_square = pygame.transform.scale(pygame.image.load("img/white_square.png"), (100, 100))
white_square_rect = img_white_square.get_rect()
white_square_rect.topleft = (330, 30)

img_red_square = pygame.transform.scale(pygame.image.load("img/red_square.png"), (155 / 2, 155 / 2))
action_red_square = pygame.transform.scale(pygame.image.load("img/red_square.png"), (100, 100))
red_square_rect = img_red_square.get_rect()
red_square_rect.topleft = (400, 30)

img_grey_square = pygame.transform.scale(pygame.image.load("img/grey_square.png"), (155 / 2, 155 / 2))
action_grey_square = pygame.transform.scale(pygame.image.load("img/grey_square.png"), (100, 100))
grey_square_rect = img_grey_square.get_rect()
grey_square_rect.topleft = (470, 30)
########
square_dict = {
    1 : action_white_square,
    2 : action_red_square,
    3 : action_grey_square
}
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
    screen.blit(bet_surface, (160, 55))
    screen.blit(money_surface, (20, 120))
def double_default():
    screen.blit(img_blue_square, ((width / 2) - 300, 200))
    screen.blit(img_blue_square, (width - 100, 200))
    screen.blit(img_white_pointer, ((width / 2) - 5, 300))
double_bet = None
def show_choice():
    if double_bet == 1:
        screen.blit(img_white_square, ((width / 2) - ((155 / 2) / 2), 200))
    elif double_bet == 2:
        screen.blit(img_red_square, ((width / 2) - ((155 / 2) / 2), 200))
    elif double_bet == 3:
        screen.blit(img_grey_square, ((width / 2) - ((155 / 2) / 2), 200))
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MuhBet")
j = 0
running = True
crashed = False
working = False
multi = 1.0
power = "off"
display = "menu"
cashout = False
ended = False
def casher():
    money += (bet * multi) - bet
def animation(color): #Roulette animation of getting the said color
    global ended
    ended = True
def choose():
    screen.blit(img_white_square, white_square_rect.topleft)
    screen.blit(img_red_square, red_square_rect.topleft)
    screen.blit(img_grey_square, grey_square_rect.topleft)
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(file, "w") as f:
                    f.write(str(money))
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if not working:
                    if minus_button_rect.collidepoint(mouse_pos):
                        if power == "off" and bet > 1:
                            bet -= 1
                    if add_button_rect.collidepoint(mouse_pos):
                        if power == "off" and bet + 1 <= money:
                            bet += 1
                    if event.button in [4, 5]:
                        continue
                    if white_square_rect.collidepoint(mouse_pos):
                        double_bet = 1
                    elif red_square_rect.collidepoint(mouse_pos):
                        double_bet = 2
                    elif grey_square_rect.collidepoint(mouse_pos):
                        double_bet = 3
                    elif back_rect.collidepoint(mouse_pos):
                        if display == "menu":
                            with open(file, "w") as f:
                                f.write(str(money))
                            running = False
                        else:
                            display = "menu"
                            power = "off"
                    elif rocket_button_rect.collidepoint(mouse_pos):
                        if display == "menu":
                            display = "rocket"
                    elif double_button_rect.collidepoint(mouse_pos):
                        if display == "menu":
                            display = "double"
                    elif power == "on":
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
            if cashout == True:
                if bet > money:
                    bet = 0
                money += (bet * multi) - bet
                cashout = False
            multi = 1.0
            screen.blit(img_poweron, poweron_rect.topleft)
            clock.tick(60)
        elif power == "on":
            rocket_pool = [1, 2, 2, 2, 3, 3, 3, 4, 4, 6, 6, 7, 7, 10, 10, 15]
            try:
                if random_float == False:
                    random_float = random.uniform(1, random.choice(rocket_pool))
            except NameError:
                random_float = random.uniform(1, random.choice(rocket_pool))
            last_random_float = random_float
            elapsed_time = clock.tick(1000)
            multi += 0.002 * (elapsed_time / 2)
            multi_surface = font.render(f"{multi:.1f}", True, (255, 255, 255))
            screen.blit(multi_surface, (width // 2 - 50, height // 2 + 50))
            if multi > random_float:
                power = "off"
                random_float = False
                multi = 0.0
                screen.blit(img_explosion, (250, 100))
                if bet > money:
                    bet = 0
                pygame.display.flip()
                random_float_surface = font.render(f"{last_random_float:.1f}", True, (255, 0 ,0))
                crashed = True
                ctimer = 0
            cashout = True
            screen.blit(img_poweroff, poweroff_rect.topleft)
        if crashed:
            with open(file, "w") as f:
                f.write(str(money))
            ctimer += 1
            screen.blit(img_rocket, (250, 100))
            screen.blit(img_explosion, (250, 100))
            multi_surface = font.render(f"{multi:.1f}", True, (255, 255, 255))
            screen.blit(random_float_surface, (width // 2 - 50, height // 2 + 50))
            if ctimer >= 100:
                crashed = False
            pygame.display.flip()
    elif display == "double":
        default()
        screen.blit(img_poweron, poweron_rect.topleft)
        try:
            screen.blit(square_dict[color_got], ((width / 2) - 100 / 2, 330))
        except NameError:
            pass
        if power == "on" and money >= bet:
            screen.blit(img_poweroff, (width / 2 - 50, 470))
            working = True
            if random.randint(0, 24) == 1:
                color_got = 1
            else:
                color_got = random.randint(2,3)
            animation(color_got)
            if ended:
                if double_bet == color_got:
                    if color_got == 1:
                        money += (bet * 14) - bet
                    else:
                        money += (bet * 2) - bet
                else:
                    money -= bet
                power = "off"
                working = False
                ended = False

        choose()
        show_choice()
        double_default()
    pygame.display.flip()
pygame.quit()
sys.exit()