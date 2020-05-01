import pygame
import time
# Choose the language
from elements_eng import ele as elements

# The list of elements
ele = elements
flag_num_ele = True
flag_symbol  = True
flag_mass    = False
flag_background   = False


# set up pygame
pygame.init()
screen = pygame.display.set_mode((80,100))
background = pygame.image.load("frame.png")

font_number = pygame.font.Font('./ttf/CallingCode-Regular.ttf', 12)
textY_number = 8 + 10
font_symbol = pygame.font.Font('./ttf/orange juice 2.0.ttf', 40)
textY_symbol= 24 + 10
font_mass = pygame.font.Font('./ttf/CallingCode-Regular.ttf', 12)
textX_mass = 25
textY_mass= 76



num_ele = len(ele)


def print_text(x,y, font, text):
    score = font.render(text, True, (0,0,0))
    screen.blit(score, (x, y))


running = True
while running:

    # Control event for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set automatically the all the position
    for i in range(num_ele):

        # First, setup screen and bakground
        screen.fill((255,255,255))

        if flag_background:
            screen.blit(background,(0,0))

        if (i+1)<10:
            textX_number = 39
        elif (i+1)<100:
            textX_number = 35
        else:
            textX_number = 31

        # print((ele[i+1]["Name"]))



        text_number_str  = "{}".format(i+1)
        textX_symbol_str = ele[i+1]["Symbol"]
        textX_mass_str   = "{:.3f}".format(ele[i+1]["Mass"])

        if len(textX_symbol_str) < 2:
            textX_symbol = 30
        else:
            textX_symbol = 19

        # print(textX_mass_str)
        if len(textX_mass_str) < 6:
            textX_mass = 23
        elif len(textX_mass_str) < 7:
            textX_mass = 20
        else:
            textX_mass = 16

        if flag_num_ele:
            print_text(textX_number, textY_number, font_number, text_number_str)

        if flag_symbol:
            print_text(textX_symbol, textY_symbol, font_symbol, textX_symbol_str)

        if flag_mass:
            print_text(textX_mass, textY_mass, font_mass, textX_mass_str)

        pygame.display.update()

        filename = "./imgs/{}.jpg".format(i+1)
        pygame.image.save(screen, filename)
        time.sleep(.2)

    running = False
