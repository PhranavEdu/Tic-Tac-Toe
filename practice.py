import pygame
import math

from pygame.examples.moveit import WIDTH

length=600
width=600

#color

white=(255,255,255)
black=(0,0,0)
win=pygame.display.set_mode((width,length))

game=True
rows=3
def draw_grid():
    gap=width//rows
    x=0
    y=0
    for i in range (rows):
        x=i*rows
    pygame.draw.line(win,black,(x,0),(x,width),3)
    pygame.draw.line(win,black,(0,x),(width,x),3)
    
#Checking if someone has won

def display_message(param):
    pass


def has_won(game_array):
    for row in range(len(game_array)):
        if (game_array[row][0][2] == game_array[row][1][2] == game_array[row][2][2]) and game_array[row][0][2] != "":
            display_message(game_array[row][0][2].upper() + " has won!")
            return True

    for col in range(len(game_array)):
        if (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2]) and game_array[0][col][2] != "":
            display_message(game_array[0][col][2].upper() + " has won!")
            return True

        if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
            display_message(game_array[0][0][2].upper() + " has won!")
            return True

    # Checking reverse diagonal
        if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
            display_message(game_array[0][2][2].upper() + " has won!")
            return True

        return False

def draw_marks(game_array=None, row=None, col=None, gap=None):
    font=pygame.font.Font(None,150)
    for row in range(len(game_array[row])):
        if game_array[row][col]!='''''':
            text=font.render(game_array[row],[col],True,black)
            x=col*gap+gap//2-text.get_width()//2

            y=row*gap+gap//2-text.get_height()//2
        win.blit(text,(x,y))

def get_cell(POS, gap=None):
    x,y=POS
    return y//gap,x//gap

def render():
    win.fill(white)
    draw_grid()

    # Drawing X's and O's
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()


def main():
    global x_turn, o_turn, images, draw

    images = []
    draw = False

    run = True

#game loop
player="x"

win.fill(white)
draw_grid()
def draw_marks(row=None, game_array=None):
    font=pygame.font.Font(None,150)
    for row in range(len(game_array[row])):
        if game_array[row][col]!='''''':
            text=font.render(game_array[row][col],True,black)
pygame.display.update()

def has_drawn(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            if game_array[i][j][2] == "":
                return False

    display_message("It's a draw!")
    return True
class Sys:
    pass


for event in pygame.event.get():
    if event.type==pygame.QUIT:
        game=False
        pygame.QUIT()
        Sys.exit()

if event.type==pygame.MOUSEBUTTONDOWN:
    row,col=get_cell(pygame.mouse.get_pos())


def initialize_grid(ROWS=None):
    dis_to_cen = WIDTH // ROWS // 2
game_array = [[None, None, None], [None, None, None], [None, None, None]]


#if game_array[rows][col]:
#game_array[rows][col]=player
#if has_won(game_array):
 #       game=False
 #       player="o" if player == "x" else "x"

    #quit the game

while game:
    win.fill(white)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.QUIT()


