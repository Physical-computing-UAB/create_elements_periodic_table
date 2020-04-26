import pygame
import time


# set up pygame
pygame.init()
screen = pygame.display.set_mode((80,100))
background = pygame.image.load("frame.png")

font_number = pygame.font.Font('CallingCode-Regular.ttf', 12)
textY_number = 8
font_symbol = pygame.font.Font('CallingCode-Regular.ttf', 40)
textY_symbol= 24
font_mass = pygame.font.Font('CallingCode-Regular.ttf', 12)
textX_mass = 25
textY_mass= 76


ele = {
    1 : {
        "Name"   : "Hidrogen",
        "Symbol" : "H",
        "Mass"   : 1.008
    } ,
    2 : {
        "Name"   : "Helium",
        "Symbol" : "He",
        "Mass"   : 4.003
    } ,
    3 : {
        "Name"   : "Litium",
        "Symbol" : "Li",
        "Mass"   : 6.941
    }
}
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
        screen.blit(background,(0,0))

        if i<10:
            textX_number = 39
        elif i<100:
            textX_number = 30
        else:
            textX_number = 25

        # print((ele[i+1]["Name"]))

        if len(ele[i+1]["Symbol"]) < 2:
            textX_symbol = 30
        else:
            textX_symbol = 19

        print_text(textX_number, textY_number, font_number, str(i+1))
        print_text(textX_symbol, textY_symbol, font_symbol, ele[i+1]["Symbol"])
        print_text(textX_mass, textY_mass, font_mass, str(ele[i+1]["Mass"]))
        pygame.display.update()

        filename = "./imgs/{}.jpg".format(i+1)
        pygame.image.save(screen, filename)
        time.sleep(2)

        running = False
