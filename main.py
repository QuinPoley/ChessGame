import pygame
from pieces import *

pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Quin's Chess Game!")
myfont = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time
colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)
colorRed = (255, 0, 0)
WHITE_PIECES = []
BLACK_PIECES = []
All_PIECES = [] # List of rects for collidepoint()
clicked_piece = [] # selected piece list will never be greater than 1

def InitializeGameOfChess():
    WHITE_PIECES.clear()
    BLACK_PIECES.clear()
    for x in range(8): # Do all the pawns
        WHITE_PIECES.append(Pawn("white", x, 2)) # X is really the letter but numbers work
        BLACK_PIECES.append(Pawn("black", x, 7))
        if (x == 0 or x == 7):
            WHITE_PIECES.append(Rook("white", x, 1))
            BLACK_PIECES.append(Rook("black", x, 8))
        elif(x == 1 or x == 6):
            WHITE_PIECES.append(Knight("white", x, 1))
            BLACK_PIECES.append(Knight("black", x, 8))
        elif(x == 2 or x == 5):
            WHITE_PIECES.append(Bishop("white", x, 1))
            BLACK_PIECES.append(Bishop("black", x, 8))
        elif(x == 3):
            WHITE_PIECES.append(Queen("white", x, 1))
            BLACK_PIECES.append(Queen("black", x, 8))
        else:
            WHITE_PIECES.append(King("white", x, 1))
            BLACK_PIECES.append(King("black", x, 8))
    for x in range(16):
        print(BLACK_PIECES[x])
    
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
    for  something in WHITE_PIECES:
        x = (something.letter * 100) + 50
        y = 850 - (something.number * 100)# 1 is first index
        rectangle = pygame.Rect(x, y, 20, 20)
        All_PIECES.append(rectangle)
        pygame.draw.rect(WIN, colorWhite, rectangle)

def drawBlack():
    for  something in BLACK_PIECES:
        x = (something.letter * 100) + 50
        y = 850 - (something.number * 100) # 1 x 100 because 1 indexed
        rectangle = pygame.Rect(x, y, 20, 20)
        All_PIECES.append(rectangle)
        pygame.draw.rect(WIN, colorBlack, rectangle)

def drawSelectedPiece():
    if(len(clicked_piece) > 0):
        pygame.draw.rect(WIN, colorRed, clicked_piece[0])

def drawChessPieces():
    drawWhite()
    drawBlack()
    drawSelectedPiece()

def drawWindow():
    WIN.fill((255,255,255))
    drawChessBoard()
    drawChessPieces()
    pygame.display.update()

def clickOnPiece(pos):
    global clicked_piece
    for s in All_PIECES:
        if s.collidepoint(pos):
            clicked_piece.clear()
            clicked_piece.append(s)
    #clicked_piece = [s for s in All_PIECES if s.collidepoint(pos)]  List Comprehensions still make no sense

def whereClick(pos):
    x, y = pos
    squareX = (x //100) + 1
    squareY = (y //100) + 1
    return (squareX, squareY)
    

def main():
    Running = True
    clock = pygame.time.Clock()
    InitializeGameOfChess()
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clickOnPiece(pos) # some time click on piece
                if(len(clicked_piece) > 0): # There is a piece selected, trying to move it
                    moveTo = whereClick(pos)
                    print(moveTo)

        clock.tick(30)
        drawWindow()

        
    pygame.quit()

if __name__ == "__main__":
    main()