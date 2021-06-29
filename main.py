from game import GameOfChess
import pygame
import sys
from pygame.constants import QUIT
from pygame.draw import rect
from pieces import *
import LegalMove
import ai
import Engine

pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode([830, 870])

pygame.display.set_caption("Quin's Chess Game!")
myfont = pygame.font.SysFont('Cambria', 30)
smallfont = pygame.font.SysFont('Times', 20)
bigTitle = pygame.font.SysFont('Times', 70, bold=True, italic=False)
clock = pygame.time
colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)
colorRed = (255, 0, 0)
colorSalmon = (255, 160, 122)
colorDarkRed  = (215, 51, 51)
colorBrown = (110, 38, 14)

#   SPRITES     #
wKing = pygame.image.load("Images/WhiteKing.png")
wQueen = pygame.image.load("Images/WhiteQueen.png")
wBishop = pygame.image.load("Images/WhiteBishop.png")
wKnight = pygame.image.load("Images/WhiteKnight.png")
wRook = pygame.image.load("Images/WhiteRook.png")
wPawn = pygame.image.load("Images/WhitePawn.png")
bKing = pygame.image.load("Images/BlackKing.png")
bQueen = pygame.image.load("Images/BlackQueen.png")
bBishop = pygame.image.load("Images/BlackBishop.png")
bKnight = pygame.image.load("Images/BlackKnight.png")
bRook = pygame.image.load("Images/BlackRook.png")
bPawn = pygame.image.load("Images/BlackPawn.png")
# ALL SPRITES #
# SCALING
wKing = pygame.transform.scale(wKing, (75, 75))
wQueen = pygame.transform.scale(wQueen, (75, 75))
wBishop = pygame.transform.scale(wBishop, (75, 75))
wKnight = pygame.transform.scale(wKnight, (75, 75))
wRook = pygame.transform.scale(wRook, (75, 75))
wPawn = pygame.transform.scale(wPawn, (75, 75))
bKing = pygame.transform.scale(bKing, (75, 75))
bQueen = pygame.transform.scale(bQueen, (75, 75))
bBishop = pygame.transform.scale(bBishop, (75, 75))
bKnight = pygame.transform.scale(bKnight, (75, 75))
bRook = pygame.transform.scale(bRook, (75, 75))
bPawn = pygame.transform.scale(bPawn, (75, 75))
# SCALING TINY
swKing = pygame.transform.scale(wKing, (15, 15))
swQueen = pygame.transform.scale(wQueen, (15, 15))
swBishop = pygame.transform.scale(wBishop, (15, 15))
swKnight = pygame.transform.scale(wKnight, (15, 15))
swRook = pygame.transform.scale(wRook, (15, 15))
swPawn = pygame.transform.scale(wPawn, (15, 15))
sbKing = pygame.transform.scale(bKing, (15, 15))
sbQueen = pygame.transform.scale(bQueen, (15, 15))
sbBishop = pygame.transform.scale(bBishop, (15, 15))
sbKnight = pygame.transform.scale(bKnight, (15, 15))
sbRook = pygame.transform.scale(bRook, (15, 15))
sbPawn = pygame.transform.scale(bPawn, (15, 15))
    
def drawChessBoard(game):
    colorTan = (210, 180, 140)
    for x in range(8): # Number of rows on a chessboard
        for y in range(8): # Number of columns on a chessboard
            if(x % 2 == 0):
                if(y % 2 == 0):
                    #Tan
                    pygame.draw.rect(WIN, colorTan, pygame.Rect((x*100), (y*100), 100, 100))
                else:
                    # Green
                    pygame.draw.rect(WIN, colorBrown, pygame.Rect((x*100), (y*100), 100, 100))
            else:
                if(y % 2 == 0):
                    #Green
                    pygame.draw.rect(WIN, colorBrown, pygame.Rect((x*100), (y*100), 100, 100))
                else:
                    #Tan
                    pygame.draw.rect(WIN, colorTan, pygame.Rect((x*100), (y*100), 100, 100))

    if(game.CurrentlySelected != None):
        selectedX = (game.CurrentlySelected.letter * 100) - 100 # 1 Indexed
        selectedY = 800 - (game.CurrentlySelected.number * 100)
        pygame.draw.rect(WIN, colorRed, pygame.Rect(selectedX, selectedY, 100, 100))
        # valid moves too
        ValidMoveSet = game.CurrentlySelected.returnLegalMoves()
        for x in range(len(ValidMoveSet)):
            if(LegalMove.isValid(ValidMoveSet[x][0], ValidMoveSet[x][1], game.CurrentlySelected, game.Black, game.White, game.PreviouslyMovingPiece)):
                validmovX = (ValidMoveSet[x][0] * 100) - 100
                validmovY = 800 - (ValidMoveSet[x][1] * 100)
                if((validmovX //100) % 2 == 0):
                    if((validmovY//100) % 2 == 0):
                        pygame.draw.rect(WIN, colorSalmon, pygame.Rect(validmovX, validmovY, 100, 100))  
                    else:
                        pygame.draw.rect(WIN, colorDarkRed, pygame.Rect(validmovX, validmovY, 100, 100))  
                else:
                    if((validmovY//100) % 2 == 0):
                        pygame.draw.rect(WIN, colorDarkRed, pygame.Rect(validmovX, validmovY, 100, 100))  
                    else:
                        pygame.draw.rect(WIN, colorSalmon, pygame.Rect(validmovX, validmovY, 100, 100))  
                  
    for x in range(8):
        rownumber = myfont.render((x+1).__str__(), False, (0, 0, 0))
        WIN.blit(rownumber,(802,(840-100*(x+1))))
        columnletter = myfont.render(chr(97+x).capitalize(), False, (0, 0, 0))
        WIN.blit(columnletter,((100*x +40),800))
        pygame.draw.line(WIN, colorBlack, (0, 100*x) , (830, 100*x))
        pygame.draw.line(WIN, colorBlack, (100*x, 0) , (100*x, 830))
    pygame.draw.line(WIN, colorBlack, (0, 800) , (830, 800))
    pygame.draw.line(WIN, colorBlack, (800, 0) , (800, 830))
    
def drawWhite(game):
    for  something in game.White:
        x = (something.letter * 100) - 100
        y = 800 - (something.number * 100)# 1 is first index
        rectangle = pygame.Surface((100, 100), pygame.SRCALPHA)
        #rectangle.fill((255, 255, 255, 0))
        if(something.__class__.__name__ == "Pawn"):
            rectangle.blit(wPawn, (10,10))
        elif(something.__class__.__name__ == "King"):
           rectangle.blit(wKing, (10,10))
        elif(something.__class__.__name__ == "Queen"):
            rectangle.blit(wQueen, (10,10))
        elif(something.__class__.__name__ == "Bishop"):
            rectangle.blit(wBishop, (10,10))
        elif(something.__class__.__name__ == "Knight"):
            rectangle.blit(wKnight, (10,10))
        elif(something.__class__.__name__ == "Rook"):
            rectangle.blit(wRook, (10,10))  
        #All_PIECES.append(rectangle)
        WIN.blit(rectangle, (x, y))

def drawBlack(game):
    for  something in game.Black:
        x = (something.letter * 100) - 100
        y = 800 - (something.number * 100)# 1 is first index
        rectangle = pygame.Surface((100, 100), pygame.SRCALPHA)
        #rectangle.fill((255, 255, 255, 0))
        if(something.__class__.__name__ == "Pawn"):
            rectangle.blit(bPawn, (10,10))
        elif(something.__class__.__name__ == "King"):
           rectangle.blit(bKing, (10,10))
        elif(something.__class__.__name__ == "Queen"):
            rectangle.blit(bQueen, (10,10))
        elif(something.__class__.__name__ == "Bishop"):
            rectangle.blit(bBishop, (10,10))
        elif(something.__class__.__name__ == "Knight"):
            rectangle.blit(bKnight, (10,10))
        elif(something.__class__.__name__ == "Rook"):
            rectangle.blit(bRook, (10,10))  
        #All_PIECES.append(rectangle)
        WIN.blit(rectangle, (x, y))

def drawSelectedPiece(game):
    if(game.CurrentlySelected != None):
        pygame.draw.rect(WIN, colorRed, (100, 100, game.CurrentlySelected.letter, game.CurrentlySelected.number))

def drawChessPieces(game):
    drawWhite(game)
    drawBlack(game)
    drawSelectedPiece(game)

def drawBottomBar(game):
    pygame.draw.rect(WIN, (76, 76, 76), pygame.Rect(0, 830, 830, 40))
    white = smallfont.render("White", False, colorWhite)
    black = smallfont.render("Black", False, colorWhite)
    #WIN.blit(turn,(625,760))
    WIN.blit(white,(700, 840))
    WIN.blit(black,(50, 840))
    if(game.WhiteTurn):
        x = 760
    else:
        x = 30
    pygame.draw.rect(WIN, (212, 175, 55), pygame.Rect(x, 847, 10, 10))
    for x in range(len(game.CapturedWhite)):
        surf = pygame.Surface((20, 20), pygame.SRCALPHA)
        if(game.CapturedWhite[x].__class__.__name__ == "Pawn"):
            surf.blit(swPawn, (0,0))
        elif(game.CapturedWhite[x].__class__.__name__ == "King"):
           surf.blit(swKing, (0,0))
        elif(game.CapturedWhite[x].__class__.__name__ == "Queen"):
            surf.blit(swQueen, (0,0))
        elif(game.CapturedWhite[x].__class__.__name__ == "Bishop"):
            surf.blit(swBishop, (0,0))
        elif(game.CapturedWhite[x].__class__.__name__ == "Knight"):
            surf.blit(swKnight, (0,0))
        elif(game.CapturedWhite[x].__class__.__name__ == "Rook"):
            surf.blit(swRook, (0,0)) 
        WIN.blit(surf, ((100 + (20*x)), 845))
        
        
    for x in range(len(game.CapturedBlack)):
        surf = pygame.Surface((20, 20), pygame.SRCALPHA)
        if(game.CapturedBlack[x].__class__.__name__ == "Pawn"):
            surf.blit(sbPawn, (0,0))
        elif(game.CapturedBlack[x].__class__.__name__ == "King"):
           surf.blit(sbKing, (0,0))
        elif(game.CapturedBlack[x].__class__.__name__ == "Queen"):
            surf.blit(sbQueen, (0,0))
        elif(game.CapturedBlack[x].__class__.__name__ == "Bishop"):
            surf.blit(sbBishop, (0,0))
        elif(game.CapturedBlack[x].__class__.__name__ == "Knight"):
            surf.blit(sbKnight, (0,0))
        elif(game.CapturedBlack[x].__class__.__name__ == "Rook"):
            surf.blit(sbRook, (0,0)) 
        WIN.blit(surf, ((680 - (20*x)), 845))

def drawWindow(game):
    WIN.fill(colorWhite)
    drawChessBoard(game)
    drawChessPieces(game)
    drawBottomBar(game)
    pygame.display.update()

def squareInLegalMoves(attemptedMove, allowedMoves):
    #is attempted move in allowed moves?
    for x in range(len(allowedMoves)):
        if(attemptedMove == allowedMoves[x]):
            return True
    return False

def printEngineEval(WHITE_PIECES, BLACK_PIECES):
    values = Engine.Eval(WHITE_PIECES, BLACK_PIECES)
    print("White Material :"+str(values[0])) 
    print("Black Material :"+str(values[1]))  
    print("White/Black Controlled Squares :"+str(values[2]))  
    print("White King Safety :"+str(values[3])) 
    print("Black King Safety :"+str(values[4]))

def drawLoadScreen():
    WIN.fill(colorBlack)
    Title = bigTitle.render("Chess", True, colorWhite)
    PlayGame = smallfont.render("Vs. Computer", True, colorWhite)
    PlayOnline = smallfont.render("Online", True, colorWhite)
    Quit = smallfont.render("Quit", True, colorWhite)
    pygame.draw.rect(WIN, colorRed, pygame.Rect(300, 450, 200, 50))
    pygame.draw.rect(WIN, colorRed, pygame.Rect(300, 520, 200, 50))
    pygame.draw.rect(WIN, colorRed, pygame.Rect(300, 590, 200, 50))
    WIN.blit(Title,(305, 305))
    WIN.blit(PlayGame,(340, 460))
    WIN.blit(PlayOnline,(340, 530))
    WIN.blit(Quit,(340, 600))
    pygame.display.update()
    

def main():
    loadScreen = True
    while loadScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if(click[0] >= 300 and click[0] <= 500):
                    if(click[1] >= 450 and click[1] <= 500): # VS AI
                        loadScreen = False
                    elif(click[1] >= 520 and click[1] <= 570): # NETWORKING
                        print("Nope.")
                    elif(click[1] >= 590 and click[1] <= 640): #NO PLAY
                        pygame.quit()
                        sys.exit()
        drawLoadScreen()
    
    Running = True
    clock = pygame.time.Clock()
    game = GameOfChess()
    Opponent = ai.ComputerOpponent()
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.SelectPiece(pygame.mouse.get_pos())
                # Okay maybe trying to move

        clock.tick(30)
        drawWindow(game)

    pygame.quit()

if __name__ == "__main__":
    main()
