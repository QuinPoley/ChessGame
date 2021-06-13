import pygame
from pygame.draw import rect
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
piece = None
WhiteTurn = True

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

def drawWindow():
    WIN.fill((255,255,255))
    drawChessBoard()
    drawChessPieces()
    turn = myfont.render("White Turn", False, (0, 0, 0)) if WhiteTurn else myfont.render("Black Turn", False, (0, 0, 0))
    WIN.blit(turn,(625,760))
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

# Make sure there is no piece on the same square that is the same color
def isValid(letter, number, movpiece): 
    if(movpiece.color == "white"):
        for x in range(len(WHITE_PIECES)):
            if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == number):
                return False
    else:
        for x in range(len(BLACK_PIECES)):
            if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == number):
                return False
    if(movpiece.__class__.__name__ == "Pawn"): # Check if diag mov is valid and if is first move for that pawn
        # DIAGONAL MOVE CHECK
        if(movpiece.color == "white" and movpiece.letter != letter): # white pawn moving diagonally
            for x in range(len(BLACK_PIECES)):
                if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == number):
                    return True
            return False # Not a capture, hence not valid
        elif(movpiece.color == "black" and movpiece.letter != letter):
            for x in range(len(WHITE_PIECES)):
                if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == number):
                    return True
            return False # Not a capture, hence not valid

        # FWD MOVE CHECK
        if(movpiece.color == "white" and (movpiece.number+1) != number and movpiece.number != 2): # white piece trying to move two squares after first move is invalid
            return False
        elif(movpiece.color == "black" and (movpiece.number-1) != number and movpiece.number != 7): # black piece trying to move two squares after first move is invalid
            return False

        # FWD MOVE CAPTURE CHECK
        if(movpiece.color == "white" and movpiece.letter == letter): # white pawn moving forward cannot capture
            for x in range(len(BLACK_PIECES)):
                if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == number):
                    return False
        elif(movpiece.color == "black" and movpiece.letter == letter): # black pawn moving forward cannot capture
            for x in range(len(WHITE_PIECES)):
                if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == number):
                    return False
            
        #FINALLY, AS AN EDGE CASE, A KNIGHT OBSTRUCTING A, C, F, H Pawns means that they cannot move two squares forward, moving throught the knight
        if(movpiece.color == "white" and (movpiece.number+1) != number):
            for x in range(len(BLACK_PIECES)): # Invalid whether it is your piece or opponents
                if(BLACK_PIECES[x].number == (movpiece.number+1) and BLACK_PIECES[x].letter == movpiece.letter): # There is a piece blocking move
                    return False
            for x in range(len(WHITE_PIECES)):
                if(WHITE_PIECES[x].number == (movpiece.number+1) and WHITE_PIECES[x].letter == movpiece.letter): # There is a piece blocking move
                    return False
        elif(movpiece.color == "black" and (movpiece.number-1) != number):
            for x in range(len(BLACK_PIECES)): # Invalid whether it is your piece or opponents
                if(BLACK_PIECES[x].number == (movpiece.number-1) and BLACK_PIECES[x].letter == movpiece.letter): # There is a piece blocking move
                    return False
            for x in range(len(WHITE_PIECES)):
                if(WHITE_PIECES[x].number == (movpiece.number-1) and WHITE_PIECES[x].letter == movpiece.letter): # There is a piece blocking move
                    return False
    return True

# Remove pieces from other color if on square
def isCapture(letter, number, color):
    if(color == "white"):
        for x in range(len(BLACK_PIECES)):
            if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == number):
                BLACK_PIECES.pop(x)
                return True # Bug where after popping off list would continue through
    else:
        for x in range(len(WHITE_PIECES)):
            if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == number):
                WHITE_PIECES.pop(x)
                return True
    return False

#pos is position of the mouse during an mousedown event
# whoTurn is a boolean that is true during whites turn and false during blacks turn
def clickOnPiece(pos, whoTurn):
    global piece
    square = whereClick(pos)
    pieceTmp = pieceAt(square, whoTurn)
    if(pieceTmp != None):
        piece = pieceTmp
    #then is there a piece on that square
    # Move pos so that it hits bounding box of that square
    #changeX =  (square[0] * 100) - 49# Modify my dumb grid so it fits pixel measurements
    #changeY = 851 - (square[1] * 100)
    #posChanged = (changeX, changeY)

    # Same code for determining which rect it falls into
    #global clicked_piece
    #for s in All_PIECES:
    #    if s.collidepoint(posChanged):
    #        clicked_piece.clear()
    #        clicked_piece.append(s)
    #clicked_piece = [s for s in All_PIECES if s.collidepoint(pos)]  List Comprehensions still make no sense
    # Finally, return the piece that was clicked on
    return piece
    

def whereClick(pos):
    x, y = pos
    squareX = (x //100) + 1
    squareY = 8 - (y //100)
    return (squareX, squareY)
    

def main():
    Running = True
    global WhiteTurn
    global piece
    clock = pygame.time.Clock()
    InitializeGameOfChess()
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                movingPiece = clickOnPiece(pos, WhiteTurn) # some time click on piece
                if(movingPiece != None): # There is a piece selected, trying to move it  len(clicked_piece) > 0 and 
                    if(WhiteTurn and movingPiece.color == "white" or not WhiteTurn and movingPiece.color == "black"): # If it is white's turn needs to be white piece moving
                        moveTo = whereClick(pos)
                        moves = movingPiece.returnLegalMoves()
                        allow = squareInLegalMoves(moveTo, moves)
                        if(isValid(moveTo[0], moveTo[1], movingPiece) and allow): # Not moving on top of teammate
                            print("Move Valid moving "+ movingPiece.__str__() + " to "+moveTo.__str__())
                            isCapture(moveTo[0], moveTo[1], movingPiece.color) # Remove any piece from other team
                            movingPiece.letter = moveTo[0]
                            movingPiece.number = moveTo[1]
                            #clicked_piece.clear()
                            piece = None 
                            WhiteTurn = False if WhiteTurn else True               

        clock.tick(30)
        drawWindow()

        
    pygame.quit()

if __name__ == "__main__":
    main()
