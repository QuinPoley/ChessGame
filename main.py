import pygame
import sys
from pygame.constants import QUIT
from pygame.draw import rect
from pygame.scrap import contains
from pieces import *
import LegalMove
import ai

pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode([800, 840])

pygame.display.set_caption("Quin's Chess Game!")
myfont = pygame.font.SysFont('Comic Sans MS', 30)
smallfont = pygame.font.SysFont('Times', 20)
bigTitle = pygame.font.SysFont('Times', 70, bold=True, italic=False)
clock = pygame.time
colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)
colorRed = (255, 0, 0)
colorSalmon = (255, 160, 122)
WHITE_PIECES = []
BLACK_PIECES = []
CAPTURED_WHITE_PIECES = []
CAPTURED_BLACK_PIECES = []
lastPiecetoMove = None
All_PIECES = [] # List of rects for collidepoint()
clicked_piece = [] # selected piece list will never be greater than 1
piece = None
WhiteTurn = True
whiteInCheck = False
blackInCheck = False
playerIsWhite = True

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


def InitializeGameOfChess():
    WHITE_PIECES.clear()
    BLACK_PIECES.clear()
    for x in range(1, 9): # Do all the pawns
        WHITE_PIECES.append(Pawn("white", x, 2)) # X is really the letter but numbers work
        BLACK_PIECES.append(Pawn("black", x, 7))
        if (x == 1 or x == 8):
            WHITE_PIECES.append(Rook("white", x, 1))
            BLACK_PIECES.append(Rook("black", x, 8))
        elif(x == 2 or x == 7):
            WHITE_PIECES.append(Knight("white", x, 1))
            BLACK_PIECES.append(Knight("black", x, 8))
        elif(x == 3 or x == 6):
            WHITE_PIECES.append(Bishop("white", x, 1))
            BLACK_PIECES.append(Bishop("black", x, 8))
        elif(x == 4):
            WHITE_PIECES.append(Queen("white", x, 1))
            BLACK_PIECES.append(Queen("black", x, 8))
        else:
            WHITE_PIECES.append(King("white", x, 1))
            BLACK_PIECES.append(King("black", x, 8))
    for x in range(16):
        print(BLACK_PIECES[x])

# Make sure there is no piece on the same square that is the same color
def isValid(letter, number, movpiece): # TODO if castles - check to make sure in between square is not check
    if(movpiece.color == "white"):
        for x in range(len(WHITE_PIECES)):
            if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == number):
                return False
    else:
        for x in range(len(BLACK_PIECES)):
            if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == number):
                return False
    if(movpiece.__class__.__name__ == "Pawn"): # Check if diag mov is valid and if is first move for that pawn
        return LegalMove.LegalforPawn(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES, lastPiecetoMove)
    elif(movpiece.__class__.__name__ == "Queen"):
        return LegalMove.LegalforQueen(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Rook"):
        return LegalMove.LegalforRook(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Bishop"):
        return LegalMove.LegalforBishop(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Knight"):
        return LegalMove.LegalforKnight(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "King"):
        return LegalMove.LegalforKing(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    return True # King legal moves like not moving into check require checks to be defined

def isValidforCheckmate(letter, number, movpiece): 
    if(movpiece.__class__.__name__ == "Pawn"):
        return LegalMove.LegalforPawnCheck(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Queen"):
        return LegalMove.LegalforQueen(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Rook"):
        return LegalMove.LegalforRook(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Bishop"):
        return LegalMove.LegalforBishop(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Knight"):
        return LegalMove.LegalforKnight(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "King"):
        return LegalMove.LegalforKing(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    return True # King legal moves like not moving into check require checks to be defined

def getPosKing(color):
    if(color == "white"):
        for x in range(len(WHITE_PIECES)):
            if(WHITE_PIECES[x].__class__.__name__ == "King"):
                return WHITE_PIECES[x]
    else:
        for x in range(len(BLACK_PIECES)):
            if(BLACK_PIECES[x].__class__.__name__ == "King"):
                return BLACK_PIECES[x]

def popKingOffList(color):
    if(color == "white"):
        for x in range(len(WHITE_PIECES)):
            if(WHITE_PIECES[x].__class__.__name__ == "King"):
                return WHITE_PIECES.pop(x)
    else:
        for x in range(len(BLACK_PIECES)):
            if(BLACK_PIECES[x].__class__.__name__ == "King"):
                return BLACK_PIECES.pop(x)

def isCheck(color, letter=-1, number=-1): # BUG WITH PAWNS, They cannot capture directly ahead, but it is a valid move, so the is check function returns true
    if(letter == -1):
        King = getPosKing(color)
        letter = King.letter
        number = King.number
    #print(letter, number)
    global whiteInCheck, blackInCheck
    if(color == "white"): # is white in check?
        for x in range(len(BLACK_PIECES)):
            moves = BLACK_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isValidforCheckmate(moves[i][0], moves[i][1], BLACK_PIECES[x])):
                    validmoves.append((moves[i][0], moves[i][1]))
            if((letter, number) in validmoves):
                whiteInCheck = True
                return True       
    else: # is black in check?
        for x in range(len(WHITE_PIECES)):
            moves = WHITE_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isValidforCheckmate(moves[i][0], moves[i][1], WHITE_PIECES[x])):
                    validmoves.append((moves[i][0], moves[i][1]))
            if((letter, number) in validmoves):
                blackInCheck = True
                return True
    return False

def getPieceAttackingKing(color):
    King = getPosKing(color)
    listOfPieces = []
    if(color == "white"): # is white in check?
        for x in range(len(BLACK_PIECES)):
            moves = BLACK_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isValid(moves[i][0], moves[i][1], BLACK_PIECES[x])):
                    validmoves.append((moves[i][0], moves[i][1]))
            if((King.letter, King.number) in validmoves):
                listOfPieces.append(BLACK_PIECES[x])      
    else: # is black in check?
        for x in range(len(WHITE_PIECES)):
            moves = WHITE_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isValid(moves[i][0], moves[i][1], WHITE_PIECES[x])):
                    validmoves.append((moves[i][0], moves[i][1]))
            if((King.letter, King.number) in validmoves):
                listOfPieces.append(WHITE_PIECES[x])
    return listOfPieces


def isCheckMate(color):
    if(not isCheck(color)):
        return False
    King = getPosKing(color)
    moves = King.returnLegalMoves()
    for x in range(len(moves)):
        #print(moves[x][0], moves[x][1])
        #print(isValid(moves[x][0], moves[x][1], King))
        if(isValid(moves[x][0], moves[x][1], King)):
            if(not isCheck(color, moves[x][0], moves[x][1])):
                return False
    attackers = getPieceAttackingKing(color)
    if(len(attackers) == 1):  # Can the piece be captured? NOTE IN THIS CASE ONLY 1 PIECE IS ATTACKING KING
        if(color == "white"):
            cancapture = isCheck("black", attackers[0].letter, attackers[0].number) # is check with args passed in is actually can a piece capture at that square
            if(cancapture):  # MAY STILL BE TRUE, IF MOVING CAPTURING PIECE CAUSES CHECK OR IF PIECE IS DEFENDED
                isdefended = isCheck("white", attackers[0].letter, attackers[0].letter) # Is the piece defended?
                if(isdefended):
                    king = popKingOffList("white") # can it be captured by some piece that is not the king?
                    canstillcapture = isCheck("black", attackers[0].letter, attackers[0].number)
                    WHITE_PIECES.append(king) # Need to put king back on list
                    if(canstillcapture): 
                        return False
                
        else:
            cancapture = isCheck("white", attackers[0].letter, attackers[0].number) # is check with args passed in is actually can a piece capture at that square
            if(cancapture):
                isdefended = isCheck("black", attackers[0].letter, attackers[0].letter) # Is the piece defended?
                if(isdefended):
                    king = popKingOffList("black") # can it be captured by some piece that is not the king?
                    canstillcapture = isCheck("white", attackers[0].letter, attackers[0].number)
                    BLACK_PIECES.append(king) # Need to put king back on list
                    if(canstillcapture):
                        return False

    # King cannot move, and piece cannot be captured. Can it be blocked?
    isBlockable = LegalMove.listofblocks(attackers, King, BLACK_PIECES, WHITE_PIECES)
    if(color == "white"):
        for x in range(len(WHITE_PIECES)):
            moves = WHITE_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isValid(moves[i][0], moves[i][1], WHITE_PIECES[x])):
                    validmoves.append((moves[i][0], moves[i][1]))
            for i in range(len(isBlockable)):
                if(isBlockable[i] in validmoves): # There is a valid move that blocks the check
                    return False
    else:
        for x in range(len(BLACK_PIECES)):
            moves = BLACK_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isValid(moves[i][0], moves[i][1], BLACK_PIECES[x])):
                    validmoves.append((moves[i][0], moves[i][1]))
            for i in range(len(isBlockable)):
                if(isBlockable[i] in validmoves): # There is a valid move that blocks the check
                    return False
    # Now we have a list of possible blocks. Can we move there?
    #if(isBlockable):
    #    return False
    return True
    
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
    global piece # Check if a piece is selected, highlight square underneath
    if(piece != None):
        selectedX = (piece.letter * 100) - 100 # 1 Indexed
        selectedY = 800 - (piece.number * 100)
        pygame.draw.rect(WIN, colorRed, pygame.Rect(selectedX, selectedY, 100, 100))
        # valid moves too
        ValidMoveSet = piece.returnLegalMoves()
        for x in range(len(ValidMoveSet)):
            if(isValid(ValidMoveSet[x][0], ValidMoveSet[x][1], piece)):
                validmovX = (ValidMoveSet[x][0] * 100) - 100
                validmovY = 800 - (ValidMoveSet[x][1] * 100)
                pygame.draw.rect(WIN, colorSalmon, pygame.Rect(validmovX, validmovY, 100, 100))
            


def drawWhite():
    for  something in WHITE_PIECES:
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

def drawBlack():
    for  something in BLACK_PIECES:
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

def drawSelectedPiece():
    if(len(clicked_piece) > 0):
        pygame.draw.rect(WIN, colorRed, clicked_piece[0])

def drawChessPieces():
    drawWhite()
    drawBlack()
    drawSelectedPiece()

def drawBottomBar():
    white = smallfont.render("White", False, colorWhite)
    black = smallfont.render("Black", False, colorWhite)
    #WIN.blit(turn,(625,760))
    WIN.blit(white,(700, 810))
    WIN.blit(black,(50, 810))
    if(WhiteTurn):
        x = 760
    else:
        x = 30
    pygame.draw.rect(WIN, (212, 175, 55), pygame.Rect(x, 817, 10, 10))
    #pygame.draw.rect(WIN, (212, 175, 55), pygame.Rect(660, 810, 20, 20))
    for x in range(len(CAPTURED_WHITE_PIECES)):
        surf = pygame.Surface((20, 20), pygame.SRCALPHA)
        if(CAPTURED_WHITE_PIECES[x].__class__.__name__ == "Pawn"):
            surf.blit(swPawn, (0,0))
        elif(CAPTURED_WHITE_PIECES[x].__class__.__name__ == "King"):
           surf.blit(swKing, (0,0))
        elif(CAPTURED_WHITE_PIECES[x].__class__.__name__ == "Queen"):
            surf.blit(swQueen, (0,0))
        elif(CAPTURED_WHITE_PIECES[x].__class__.__name__ == "Bishop"):
            surf.blit(swBishop, (0,0))
        elif(CAPTURED_WHITE_PIECES[x].__class__.__name__ == "Knight"):
            surf.blit(swKnight, (0,0))
        elif(CAPTURED_WHITE_PIECES[x].__class__.__name__ == "Rook"):
            surf.blit(swRook, (0,0)) 
        WIN.blit(surf, ((100 + (20*x)), 815))
        
        
    for x in range(len(CAPTURED_BLACK_PIECES)):
        surf = pygame.Surface((20, 20), pygame.SRCALPHA)
        if(CAPTURED_BLACK_PIECES[x].__class__.__name__ == "Pawn"):
            surf.blit(sbPawn, (0,0))
        elif(CAPTURED_BLACK_PIECES[x].__class__.__name__ == "King"):
           surf.blit(sbKing, (0,0))
        elif(CAPTURED_BLACK_PIECES[x].__class__.__name__ == "Queen"):
            surf.blit(sbQueen, (0,0))
        elif(CAPTURED_BLACK_PIECES[x].__class__.__name__ == "Bishop"):
            surf.blit(sbBishop, (0,0))
        elif(CAPTURED_BLACK_PIECES[x].__class__.__name__ == "Knight"):
            surf.blit(sbKnight, (0,0))
        elif(CAPTURED_BLACK_PIECES[x].__class__.__name__ == "Rook"):
            surf.blit(sbRook, (0,0)) 
        WIN.blit(surf, ((680 - (20*x)), 815))

def drawWindow():
    WIN.fill((76, 76, 76))
    drawChessBoard()
    drawChessPieces()
    drawBottomBar()
    pygame.display.update()

def pieceAt(tupSquare, whoTurn):
    Xval, Yval = tupSquare
    if(whoTurn):
        for x in range(len(WHITE_PIECES)): # Is there a white piece on that square
            if(WHITE_PIECES[x].letter == Xval and WHITE_PIECES[x].number == Yval):
                return WHITE_PIECES[x]
    else:
        for x in range(len(BLACK_PIECES)): # Is there a black piece on that square
            if(BLACK_PIECES[x].letter == Xval and BLACK_PIECES[x].number == Yval):
                return BLACK_PIECES[x]
    return None

def squareInLegalMoves(attemptedMove, allowedMoves):
    #is attempted move in allowed moves?
    for x in range(len(allowedMoves)):
        if(attemptedMove == allowedMoves[x]):
            return True
    return False

def moveRookDuringCastle(color, istoRight):
    default = 1
    movingTo = 4
    if(istoRight):
        default = 8
        movingTo = 6
    if(color == "white"):
        for x in range(len(WHITE_PIECES)):
            if(WHITE_PIECES[x].number == 1 and WHITE_PIECES[x].letter == default):
                WHITE_PIECES[x].letter = movingTo # Move Rook to other side
    else:
        for x in range(len(BLACK_PIECES)):
            if(BLACK_PIECES[x].number == 8 and BLACK_PIECES[x].letter == default):
                BLACK_PIECES[x].letter = movingTo # Move Rook to other side

# Remove pieces from other color if on square
def isCapture(letter, number, piece):
    if(piece.color == "white"):
        for x in range(len(BLACK_PIECES)):
            if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == number):
                CAPTURED_BLACK_PIECES.append(BLACK_PIECES[x])
                return BLACK_PIECES.pop(x) 
        if(lastPiecetoMove.__class__.__name__ == "Pawn" and piece.__class__.__name__ == "Pawn" and lastPiecetoMove.letter == letter and lastPiecetoMove.number == (number-1)): # CAPTURE
            for x in range(len(BLACK_PIECES)): # Find black pawn at letter, number -1
                if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == (number-1)):
                    CAPTURED_BLACK_PIECES.append(BLACK_PIECES[x])
                    return BLACK_PIECES.pop(x)
    else:
        for x in range(len(WHITE_PIECES)):
            if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == number):
                CAPTURED_WHITE_PIECES.append(WHITE_PIECES[x])
                return WHITE_PIECES.pop(x)
        if(lastPiecetoMove.__class__.__name__ == "Pawn" and piece.__class__.__name__ == "Pawn" and lastPiecetoMove.letter == letter and lastPiecetoMove.number == (number+1)): # CAPTURE
            for x in range(len(WHITE_PIECES)): # Find black pawn at letter, number +_1
                if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == (number+1)):
                    CAPTURED_WHITE_PIECES.append(CAPTURED_WHITE_PIECES[x])
                    return CAPTURED_WHITE_PIECES.pop(x)
    return None

#pos is position of the mouse during an mousedown event
# whoTurn is a boolean that is true during whites turn and false during blacks turn
def clickOnPiece(pos, whoTurn):
    global piece
    global whiteInCheck
    global blackInCheck
    #if(whiteInCheck):
    #    piece = getPosKing("white")
    #    return piece # If in check cannot select another piece UNLESS it can capture or block check
    #elif(blackInCheck):
    #    piece = getPosKing("black")
    #    return piece # If in check cannot select another piece
    square = whereClick(pos)
    pieceTmp = pieceAt(square, whoTurn)
    if(pieceTmp != None):
        piece = pieceTmp
    return piece
    

def whereClick(pos):
    x, y = pos
    squareX = (x //100) + 1
    squareY = 8 - (y //100)
    return (squareX, squareY)

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
    notCheck = True
    global WhiteTurn
    global piece
    global lastPiecetoMove
    clock = pygame.time.Clock()
    InitializeGameOfChess()
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                movingPiece = clickOnPiece(pos, WhiteTurn) # some time click on piece
                notCheck = True
                if(movingPiece != None): # There is a piece selected, trying to move it  len(clicked_piece) > 0 and 
                    if(WhiteTurn and movingPiece.color == "white" or not WhiteTurn and movingPiece.color == "black"): # If it is white's turn needs to be white piece moving
                        moveTo = whereClick(pos)
                        moves = movingPiece.returnLegalMoves()
                        allow = squareInLegalMoves(moveTo, moves)
                        color = "black" if WhiteTurn else "white"
                        altcolor = "white" if WhiteTurn else "black" #current moving
                        if(movingPiece.__class__.__name__ == "King"):
                            notCheck = not (isCheck(altcolor, moveTo[0], moveTo[1])) # King cannot move into check
                        if(isValid(moveTo[0], moveTo[1], movingPiece) and allow and notCheck): # Not moving on top of teammate and cannot move into check
                            wasJust = movingPiece.letter, movingPiece.number
                            oldPiece = isCapture(moveTo[0], moveTo[1], movingPiece)
                            attacker = getPieceAttackingKing(altcolor)
                            if(movingPiece.__class__.__name__ == "King" and (movingPiece.letter+2) == moveTo[0]):
                                moveRookDuringCastle(movingPiece.color, True)
                                print("Castles")
                            if(movingPiece.__class__.__name__ == "King" and (movingPiece.letter-2) == moveTo[0]):
                                moveRookDuringCastle(movingPiece.color, False)
                                print("Castles")
                            isfirst = movingPiece.move(moveTo[0], moveTo[1])
                            if(isCheck(altcolor)):
                                if(not (len(attacker) == 1 and attacker[0].letter == moveTo[0] and attacker[0].number == moveTo[1])):
                                    movingPiece.letter, movingPiece.number = wasJust
                                    if(isfirst): # first move from the piece and was not valid, set hasMoved back to false
                                        movingPiece.hasMoved = False
                                    if(oldPiece != None and WhiteTurn):
                                        BLACK_PIECES.append(oldPiece) # Tried to capture but not a valid move
                                        CAPTURED_BLACK_PIECES.pop()
                                    elif(oldPiece != None):
                                        WHITE_PIECES.append(oldPiece)
                                        CAPTURED_WHITE_PIECES.pop()
                                    break
                            #clicked_piece.clear()
                            print(movingPiece.color + movingPiece.__class__.__name__ + " @"+ chr(wasJust[0]+96) +","+str(wasJust[1]) +" to "+chr(moveTo[0]+96)+","+str(moveTo[1]))
                            lastPiecetoMove = movingPiece
                              # Remove any piece from other team
                            #print(getPieceAttackingKing("white"))
                            #print(getPieceAttackingKing("black"))
                            if(isCheckMate(color)):
                                print("Checkmate")
                                piece = None
                                drawWindow()
                                Winner = myfont.render(altcolor+" wins!", False, colorBlack)
                                WIN.blit(Winner, (350, 425))
                                pygame.display.update()
                                while(True):
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                            elif(isCheck(color)):
                                print("Check")
                            piece = None 
                            WhiteTurn = False if WhiteTurn else True                
        clock.tick(30)
        drawWindow()
       

        
    pygame.quit()

if __name__ == "__main__":
    main()
