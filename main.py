import pygame
from pieces import *

pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Quin's Chess Game!")
myfont = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time
WHITE_PIECES = []
DARK_PIECES = []

def InitializeGameOfChess():
    WHITE_PIECES.clear()
    DARK_PIECES.clear()
    for x in range(8): # Do all the pawns
        WHITE_PIECES.append(Pawn("white", x, 2)) # X is really the letter but numbers work
        DARK_PIECES.append(Pawn("black", x, 7))
    
def drawChessBoard():
    colorGreen = (20, 197, 20)
    colorTan = (210, 180, 140)
    for x in range(8): # Number of rows on a chessboard
        for y in range(8): # Number of columns on a chessboard
            if(x % 2 == 0):
                if(y % 2 == 0):
                    #Tan
                    pygame.draw.rect(WIN, colorTan, pygame.Rect((x*100), (y*100), 100, 100))
                else:
                    # Green
                    pygame.draw.rect(WIN, colorGreen, pygame.Rect((x*100), (y*100), 100, 100))
            else:
                if(y % 2 == 0):
                    #Green
                    pygame.draw.rect(WIN, colorGreen, pygame.Rect((x*100), (y*100), 100, 100))
                else:
                    #Tan
                    pygame.draw.rect(WIN, colorTan, pygame.Rect((x*100), (y*100), 100, 100))
    for x in range(8):
        rownumber = myfont.render((x+1).__str__(), False, (0, 0, 0))
        WIN.blit(rownumber,(5,(750-100*x)))
        columnletter = myfont.render(chr(97+x).capitalize(), False, (0, 0, 0))
        WIN.blit(columnletter,((100*x +70),0))

def drawWhite():
    print()

def drawBlack():
    print()

def drawChessPieces():
    drawWhite()
    drawBlack()

def drawWindow():
    WIN.fill((255,255,255))
    drawChessBoard()
    #drawChessPieces()
    pygame.display.update()

def main():
    Running = True
    clock = pygame.time.Clock()
    InitializeGameOfChess()
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        clock.tick(60)
        drawWindow()

        
    pygame.quit()

if __name__ == "__main__":
    main()