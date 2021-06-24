def LegalforPawn(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES, lastpiece):
    # DIAGONAL MOVE CHECK
    if((letter < 1 or letter > 8) or (number < 1 or number > 8)):
        return False
    if(movpiece.color == "white" and movpiece.letter != letter): # white pawn moving diagonally
            for x in range(len(BLACK_PIECES)):
                if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == number):
                    return True
                elif(lastpiece.__class__.__name__ == "Pawn"): # En passant check
                    if(lastpiece.letter == letter and lastpiece.number == (number-1) and lastpiece.number == 5): # Valid
                        return True
            return False # Not a capture, hence not valid
    elif(movpiece.color == "black" and movpiece.letter != letter):
            for x in range(len(WHITE_PIECES)):
                if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == number):
                    return True
                elif(lastpiece.__class__.__name__ == "Pawn"): # En passant
                    if(lastpiece.letter == letter and lastpiece.number == (number+1) and lastpiece.number == 4):
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

def LegalforQueen(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES):
    numberMovesX = abs(letter - movpiece.letter)
    numberMovesY = abs(number - movpiece.number)
    if((letter < 1 or letter > 8) or (number < 1 or number > 8)):
        return False
    if(numberMovesX == 0): # Staying in same column, check if theres a piece between queen and desired square
        if(number > movpiece.number): # Moving up the grid, add
            for x in range(1, numberMovesY):
                for i in range(len(BLACK_PIECES)):
                    if((movpiece.number+x) == BLACK_PIECES[i].number and movpiece.letter == BLACK_PIECES[i].letter):
                        return False
                for i in range(len(WHITE_PIECES)):
                    if((movpiece.number+x) == WHITE_PIECES[i].number and movpiece.letter == WHITE_PIECES[i].letter):
                        return False
                # Square 
                # movpiece.number + x
                # movpiece.letter
        else:   # Moving down subtract
            for x in range(1, numberMovesY):
                for i in range(len(BLACK_PIECES)):
                    if((movpiece.number-x) == BLACK_PIECES[i].number and movpiece.letter == BLACK_PIECES[i].letter):
                        return False
                for i in range(len(WHITE_PIECES)):
                    if((movpiece.number-x) == WHITE_PIECES[i].number and movpiece.letter == WHITE_PIECES[i].letter):
                        return False


    elif(numberMovesY == 0):  # Staying in same row, check if theres a piece between queen and desired square
        if(letter > movpiece.letter): # Moving right the grid, add
            for x in range(1, numberMovesX):
                for i in range(len(BLACK_PIECES)):
                    if((movpiece.letter+x) == BLACK_PIECES[i].letter and movpiece.number == BLACK_PIECES[i].number):
                        return False
                for i in range(len(WHITE_PIECES)):
                    if((movpiece.letter+x) == WHITE_PIECES[i].letter and movpiece.number == WHITE_PIECES[i].number):
                        return False
                # Square 
                # movpiece.number + x
                # movpiece.letter
        else:   # Moving down subtract
            for x in range(1, numberMovesX):
                for i in range(len(BLACK_PIECES)):
                    if((movpiece.letter-x) == BLACK_PIECES[i].letter and movpiece.number == BLACK_PIECES[i].number):
                        return False
                for i in range(len(WHITE_PIECES)):
                    if((movpiece.letter-x) == WHITE_PIECES[i].letter and movpiece.number == WHITE_PIECES[i].number):
                        return False


    elif(numberMovesX != 0 and numberMovesY != 0 and numberMovesY == numberMovesX):
        if(number > movpiece.number): # Moving up the grid, add
            if(letter > movpiece.letter): # Moving to the right add
                for x in range(1, numberMovesX):
                    for i in range(len(BLACK_PIECES)):
                        if((movpiece.letter+x) == BLACK_PIECES[i].letter and (movpiece.number+x) == BLACK_PIECES[i].number):
                            return False
                    for i in range(len(WHITE_PIECES)):
                        if((movpiece.letter+x) == WHITE_PIECES[i].letter and (movpiece.number+x) == WHITE_PIECES[i].number):
                            return False
            else: # Moving to the left, subtract from letter
                for x in range(1, numberMovesX):
                    for i in range(len(BLACK_PIECES)):
                        if((movpiece.letter-x) == BLACK_PIECES[i].letter and (movpiece.number+x) == BLACK_PIECES[i].number):
                            return False
                    for i in range(len(WHITE_PIECES)):
                        if((movpiece.letter-x) == WHITE_PIECES[i].letter and (movpiece.number+x) == WHITE_PIECES[i].number):
                            return False

        else: # Moving down the grid, subtract from number
            if(letter > movpiece.letter): # Moving to the right add to letter
                for x in range(1, numberMovesX):
                    for i in range(len(BLACK_PIECES)):
                        if((movpiece.letter+x) == BLACK_PIECES[i].letter and (movpiece.number-x) == BLACK_PIECES[i].number):
                            return False
                    for i in range(len(WHITE_PIECES)):
                        if((movpiece.letter+x) == WHITE_PIECES[i].letter and (movpiece.number-x) == WHITE_PIECES[i].number):
                            return False
            else: # Moving to the left, subtract from letter
                for x in range(1, numberMovesX):
                    for i in range(len(BLACK_PIECES)):
                        if((movpiece.letter-x) == BLACK_PIECES[i].letter and (movpiece.number-x) == BLACK_PIECES[i].number):
                            return False
                    for i in range(len(WHITE_PIECES)):
                        if((movpiece.letter-x) == WHITE_PIECES[i].letter and (movpiece.number-x) == WHITE_PIECES[i].number):
                            return False
    return True

def LegalforRook(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES):
    numberMovesX = abs(letter - movpiece.letter)
    numberMovesY = abs(number - movpiece.number)
    if((letter < 1 or letter > 8) or (number < 1 or number > 8)):
        return False
    if(numberMovesX == 0): # Staying in same column, check if theres a piece between queen and desired square
        if(number > movpiece.number): # Moving up the grid, add
            for x in range(1, numberMovesY):
                for i in range(len(BLACK_PIECES)):
                    if((movpiece.number+x) == BLACK_PIECES[i].number and movpiece.letter == BLACK_PIECES[i].letter):
                        return False
                for i in range(len(WHITE_PIECES)):
                    if((movpiece.number+x) == WHITE_PIECES[i].number and movpiece.letter == WHITE_PIECES[i].letter):
                        return False
                # Square 
                # movpiece.number + x
                # movpiece.letter
        else:   # Moving down subtract
            for x in range(1, numberMovesY):
                for i in range(len(BLACK_PIECES)):
                    if((movpiece.number-x) == BLACK_PIECES[i].number and movpiece.letter == BLACK_PIECES[i].letter):
                        return False
                for i in range(len(WHITE_PIECES)):
                    if((movpiece.number-x) == WHITE_PIECES[i].number and movpiece.letter == WHITE_PIECES[i].letter):
                        return False


    elif(numberMovesY == 0):  # Staying in same row, check if theres a piece between queen and desired square
        if(letter > movpiece.letter): # Moving right the grid, add
            for x in range(1, numberMovesX):
                for i in range(len(BLACK_PIECES)):
                    if((movpiece.letter+x) == BLACK_PIECES[i].letter and movpiece.number == BLACK_PIECES[i].number):
                        return False
                for i in range(len(WHITE_PIECES)):
                    if((movpiece.letter+x) == WHITE_PIECES[i].letter and movpiece.number == WHITE_PIECES[i].number):
                        return False
                # Square 
                # movpiece.number + x
                # movpiece.letter
        else:   # Moving down subtract
            for x in range(1, numberMovesX):
                for i in range(len(BLACK_PIECES)):
                    if((movpiece.letter-x) == BLACK_PIECES[i].letter and movpiece.number == BLACK_PIECES[i].number):
                        return False
                for i in range(len(WHITE_PIECES)):
                    if((movpiece.letter-x) == WHITE_PIECES[i].letter and movpiece.number == WHITE_PIECES[i].number):
                        return False
    return True

def LegalforBishop(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES):
    numberMovesX = abs(letter - movpiece.letter)
    numberMovesY = abs(number - movpiece.number)
    if((letter < 1 or letter > 8) or (number < 1 or number > 8)):
        return False
    if(numberMovesX != numberMovesX):
        return False
    if(number > movpiece.number): # Moving up the grid, add
        if(letter > movpiece.letter): # Moving to the right add
                for x in range(1, numberMovesX):
                    for i in range(len(BLACK_PIECES)):
                        if((movpiece.letter+x) == BLACK_PIECES[i].letter and (movpiece.number+x) == BLACK_PIECES[i].number):
                            return False
                    for i in range(len(WHITE_PIECES)):
                        if((movpiece.letter+x) == WHITE_PIECES[i].letter and (movpiece.number+x) == WHITE_PIECES[i].number):
                            return False
        else: # Moving to the left, subtract from letter
                for x in range(1, numberMovesX):
                    for i in range(len(BLACK_PIECES)):
                        if((movpiece.letter-x) == BLACK_PIECES[i].letter and (movpiece.number+x) == BLACK_PIECES[i].number):
                            return False
                    for i in range(len(WHITE_PIECES)):
                        if((movpiece.letter-x) == WHITE_PIECES[i].letter and (movpiece.number+x) == WHITE_PIECES[i].number):
                            return False

    else: # Moving down the grid, subtract from number
        if(letter > movpiece.letter): # Moving to the right add to letter
            for x in range(1, numberMovesX):
                for i in range(len(BLACK_PIECES)):
                    if((movpiece.letter+x) == BLACK_PIECES[i].letter and (movpiece.number-x) == BLACK_PIECES[i].number):
                        return False
                for i in range(len(WHITE_PIECES)):
                    if((movpiece.letter+x) == WHITE_PIECES[i].letter and (movpiece.number-x) == WHITE_PIECES[i].number):
                        return False
        else: # Moving to the left, subtract from letter
            for x in range(1, numberMovesX):
                for i in range(len(BLACK_PIECES)):
                    if((movpiece.letter-x) == BLACK_PIECES[i].letter and (movpiece.number-x) == BLACK_PIECES[i].number):
                        return False
                for i in range(len(WHITE_PIECES)):
                    if((movpiece.letter-x) == WHITE_PIECES[i].letter and (movpiece.number-x) == WHITE_PIECES[i].number):
                        return False
    return True

def LegalforKnight(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES):
    if((letter < 1 or letter > 8) or (number < 1 or number > 8)):
        return False
    return True # Can jump over stuff, so this is pretty much always true

def LegalforKing(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES):
    if((letter < 1 or letter > 8) or (number < 1 or number > 8)):
        return False

    if(letter == (movpiece.letter+2)):  # Trying to castle
        rook = None
        king = None
        if(movpiece.color == "white"):
            # Spaces 6,1 and 7,1 must be empty and both rook at 8,1 and king cannot have moved
            for x in range(len(WHITE_PIECES)):
                if((WHITE_PIECES[x].letter == 6 and WHITE_PIECES[x].number == 1) or (WHITE_PIECES[x].letter == 7 and WHITE_PIECES[x].number == 1)):
                    return False
                elif(WHITE_PIECES[x].letter == 8 and WHITE_PIECES[x].number == 1 and WHITE_PIECES[x].hasMoved == False):
                    rook = WHITE_PIECES[x]
                elif(WHITE_PIECES[x].letter == 5 and WHITE_PIECES[x].number == 1 and WHITE_PIECES[x].hasMoved == False):
                    king = WHITE_PIECES[x]
            for x in range(len(BLACK_PIECES)): # Not that its all that likely, but I guess there cant be a black piece there too
                if((BLACK_PIECES[x].letter == 6 and BLACK_PIECES[x].number == 1) or (BLACK_PIECES[x].letter == 7 and BLACK_PIECES[x].number == 1)):   # TODO Check if each square is check, because if so, cannot castle
                    return False
            if(rook == None or king == None): # One of the pieces was moved or captured
                return False
        else:
            # Spaces 6,8 and 7,8 must be empty and both rook at 8,8 and king cannot have moved
            for x in range(len(WHITE_PIECES)):
                if((WHITE_PIECES[x].letter == 6 and WHITE_PIECES[x].number == 8) or (WHITE_PIECES[x].letter == 7 and WHITE_PIECES[x].number == 8)):  # TODO Check if each square is check, because if so, cannot castle
                    return False
            for x in range(len(BLACK_PIECES)): 
                if((BLACK_PIECES[x].letter == 6 and BLACK_PIECES[x].number == 8) or (BLACK_PIECES[x].letter == 7 and BLACK_PIECES[x].number == 8)):  
                    return False
                elif(BLACK_PIECES[x].letter == 8 and BLACK_PIECES[x].number == 8 and BLACK_PIECES[x].hasMoved == False):
                    rook = BLACK_PIECES[x]
                elif(BLACK_PIECES[x].letter == 5 and BLACK_PIECES[x].number == 8 and BLACK_PIECES[x].hasMoved == False):
                    king = BLACK_PIECES[x]
            if(rook == None or king == None): # One of the pieces was moved or captured
                return False

    elif(letter == (movpiece.letter-2)):   # Trying to castle
        rook = None
        king = None
        if(movpiece.color == "white"):
            # Spaces 2,1  3,1   4,1 must be empty and both rook at 1,1 and king cannot have moved
            for x in range(len(WHITE_PIECES)):
                if((WHITE_PIECES[x].letter == 4 and WHITE_PIECES[x].number == 1) or (WHITE_PIECES[x].letter == 3 and WHITE_PIECES[x].number == 1) or (WHITE_PIECES[x].letter == 2 and WHITE_PIECES[x].number == 1)):
                    return False
                elif(WHITE_PIECES[x].letter == 1 and WHITE_PIECES[x].number == 1 and WHITE_PIECES[x].hasMoved == False):
                    rook = WHITE_PIECES[x]
                elif(WHITE_PIECES[x].letter == 5 and WHITE_PIECES[x].number == 1 and WHITE_PIECES[x].hasMoved == False):
                    king = WHITE_PIECES[x]
            for x in range(len(BLACK_PIECES)): # TODO Check if each square is check, because if so, cannot castle
                if((BLACK_PIECES[x].letter == 4 and BLACK_PIECES[x].number == 1) or (BLACK_PIECES[x].letter == 3 and BLACK_PIECES[x].number == 1) or (BLACK_PIECES[x].letter == 2 and BLACK_PIECES[x].number == 1)):
                    return False
            if(rook == None or king == None): # One of the pieces was moved or captured
                return False
        else:
            # Spaces 2,8  3,8   4,8 must be empty and both rook at 1,8 and king cannot have moved
            for x in range(len(WHITE_PIECES)): # TODO Check if each square is check, because if so, cannot castle
                if((WHITE_PIECES[x].letter == 4 and WHITE_PIECES[x].number == 8) or (WHITE_PIECES[x].letter == 3 and WHITE_PIECES[x].number == 8) or (WHITE_PIECES[x].letter == 2 and WHITE_PIECES[x].number == 8)): 
                    return False
            for x in range(len(BLACK_PIECES)): 
                if((BLACK_PIECES[x].letter == 4 and BLACK_PIECES[x].number == 8) or (BLACK_PIECES[x].letter == 3 and BLACK_PIECES[x].number == 8) or (BLACK_PIECES[x].letter == 2 and BLACK_PIECES[x].number == 8)):
                    return False
                elif(BLACK_PIECES[x].letter == 1 and BLACK_PIECES[x].number == 8 and BLACK_PIECES[x].hasMoved == False):
                    rook = BLACK_PIECES[x]
                elif(BLACK_PIECES[x].letter == 5 and BLACK_PIECES[x].number == 8 and BLACK_PIECES[x].hasMoved == False):
                    king = BLACK_PIECES[x]
            if(rook == None or king == None): # One of the pieces was moved or captured
                return False
    return True

def listofblocks(att, king):
    if(len(att) > 1 or att[0].__class__.__name__ == "Knight" or att[0].__class__.__name__ == "Pawn"): # Multiple pieces attacking or knight/Pawn, which cannot be blocked only captured
        return []
    attX = att[0].letter
    attY = att[0].number
    kingX = king.letter
    kingY = king.number
    listofValidBlocks = []

    if(attX == kingX): # Same column, block by being in same letter in between numbers
        
        if(attY > kingY):
            for x in range(kingY+1, attY):
                listofValidBlocks.append((kingX, x)) # square between king and attacker
        else:
             for x in range(attY+1, kingY):
                listofValidBlocks.append((kingX, x))

    elif(attY == kingY): # Same row, block by being in same number in between letters
        if(attX > kingX):
            for x in range(kingX+1, attX):
                listofValidBlocks.append((x, kingY)) # square between king and attacker
        else:
             for x in range(attX+1, kingX):
                listofValidBlocks.append((x, kingY))

    # Diagonal check, but where from
    elif(attX > kingX and attY > kingY):    # King is down and to the left of piece
        difference = attX - kingX
        for x in range(1, difference):
            listofValidBlocks.append((kingX+x, kingY+x))
    elif(attX < kingX and attY > kingY):    # King is down and to the right of piece
        difference = kingX - attX
        for x in range(1, difference):
            listofValidBlocks.append((kingX-x, kingY+x))
    elif(attX > kingX and attY < kingY):    # King is up and to the left of piece
        difference = attX - kingX
        for x in range(1, difference):
            listofValidBlocks.append((kingX+x, kingY-x))
    elif(attX < kingX and attY < kingY):    # King is up and to the right of piece
        difference = kingX - attX
        for x in range(1, difference):
            listofValidBlocks.append((kingX-x, kingY-x))

    return listofValidBlocks

def LegalforPawnCheck(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES): # Basically can a pawn capture
    # DIAGONAL MOVE CHECK
    if((letter < 1 or letter > 8) or (number < 1 or number > 8)):
        return False
    if(movpiece.color == "white" and movpiece.letter != letter): # white pawn moving diagonally
            return True
    elif(movpiece.color == "black" and movpiece.letter != letter):
            return True
    return False    

def getPieceAttackingKing(color, WHITE_PIECES, BLACK_PIECES, lastPiecetoMove):
    King = None
    if(color == "white"):
        King = getPosKing(WHITE_PIECES)
    else:
        King = getPosKing(BLACK_PIECES)
    listOfPieces = []
    if(color == "white"): # is white in check?
        for x in range(len(BLACK_PIECES)):
            moves = BLACK_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isValid(moves[i][0], moves[i][1], BLACK_PIECES[x], BLACK_PIECES, WHITE_PIECES, lastPiecetoMove)):
                    validmoves.append((moves[i][0], moves[i][1]))
            if((King.letter, King.number) in validmoves):
                listOfPieces.append(BLACK_PIECES[x])      
    else: # is black in check?
        for x in range(len(WHITE_PIECES)):
            moves = WHITE_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isValid(moves[i][0], moves[i][1], WHITE_PIECES[x], BLACK_PIECES, WHITE_PIECES, lastPiecetoMove)):
                    validmoves.append((moves[i][0], moves[i][1]))
            if((King.letter, King.number) in validmoves):
                listOfPieces.append(WHITE_PIECES[x])
    return listOfPieces

# Remove pieces from other color if on square
def isCapture(letter, number, piece, BLACK_PIECES, WHITE_PIECES, CAPTURED_BLACK_PIECES, CAPTURED_WHITE_PIECES, lastPiecetoMove):
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
                    CAPTURED_WHITE_PIECES.append(WHITE_PIECES[x])
                    return WHITE_PIECES.pop(x)
    return None

def isSquareCapturable(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES): 
    if(movpiece.__class__.__name__ == "Pawn"):
        return LegalforPawnCheck(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Queen"):
        return LegalforQueen(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Rook"):
        return LegalforRook(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Bishop"):
        return LegalforBishop(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Knight"):
        return LegalforKnight(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "King"):
        return LegalforKing(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    return True # King legal moves like not moving into check require checks to be defined

def isSafe(color, letter, number, BLACK_PIECES, WHITE_PIECES): # BUG WITH PAWNS, They cannot capture directly ahead, but it is a valid move, so the is check function returns true FIXED
    if(color == "white"): # is white in check?
        for x in range(len(BLACK_PIECES)):
            moves = BLACK_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isSquareCapturable(moves[i][0], moves[i][1], BLACK_PIECES[x], BLACK_PIECES, WHITE_PIECES)):
                    validmoves.append((moves[i][0], moves[i][1]))
            if((letter, number) in validmoves):
                return True       
    else: # is black in check?
        for x in range(len(WHITE_PIECES)):
            moves = WHITE_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isSquareCapturable(moves[i][0], moves[i][1], WHITE_PIECES[x], BLACK_PIECES, WHITE_PIECES)):
                    validmoves.append((moves[i][0], moves[i][1]))
            if((letter, number) in validmoves):
                return True
    return False

# Make sure there is no piece on the same square that is the same color
def isValid(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES, lastPiecetoMove, blackcheck=False, whitecheck=False): # TODO if castles - check to make sure in between square is not check
    if(blackcheck or whitecheck):
        #somebody in check - better be the person moving. Otherwise I screwed up.
        if((blackcheck and lastPiecetoMove.color == "black") or (whitecheck and lastPiecetoMove.color == "white")):
            print("Yeah, I screwed up. Should be game over.")
            return False
        else:
            attackers = getPieceAttackingKing(movpiece.color, WHITE_PIECES, BLACK_PIECES, lastPiecetoMove)
            king = None
            if(movpiece.color == "white"):
                king = getPosKing(WHITE_PIECES)
            else:
                king = getPosKing(BLACK_PIECES)
            allowedmoves = listofblocks(attackers, king)
            if(not (letter, number) in allowedmoves and not movpiece.__class__.__name__ == "King"):
                return False
            # letter and number must be in list of blocks. OR movpiece must be king.
    if(movpiece.color == "white"):
        for x in range(len(WHITE_PIECES)):
            if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == number):
                return False
    else:
        for x in range(len(BLACK_PIECES)):
            if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == number):
                return False
    if(movpiece.__class__.__name__ == "Pawn"): # Check if diag mov is valid and if is first move for that pawn
        return LegalforPawn(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES, lastPiecetoMove)
    elif(movpiece.__class__.__name__ == "Queen"):
        return LegalforQueen(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Rook"):
        return LegalforRook(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Bishop"):
        return LegalforBishop(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "Knight"):
        return LegalforKnight(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    elif(movpiece.__class__.__name__ == "King"):
        return LegalforKing(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)
    return True # King legal moves like not moving into check require checks to be defined

def getPosKing(ListOPieces):
    for x in range(len(ListOPieces)):
        if(ListOPieces[x].__class__.__name__ == "King"):
            return ListOPieces[x]
    
def causesCheck(color, BLACK_PIECES, WHITE_PIECES):
    King = None
    if(color == "white"):
        King = getPosKing(WHITE_PIECES)
    else:
        King = getPosKing(BLACK_PIECES)
    letter = King.letter
    number = King.number
    if(color == "white"): # is white in check?
        for x in range(len(BLACK_PIECES)):
            moves = BLACK_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isSquareCapturable(moves[i][0], moves[i][1], BLACK_PIECES[x], BLACK_PIECES, WHITE_PIECES)):
                    validmoves.append((moves[i][0], moves[i][1]))
            if((letter, number) in validmoves):
                return True       
    else: # is black in check?
        for x in range(len(WHITE_PIECES)):
            moves = WHITE_PIECES[x].returnLegalMoves()
            validmoves = []
            for i in range(len(moves)):
                if(isSquareCapturable(moves[i][0], moves[i][1], WHITE_PIECES[x], BLACK_PIECES, WHITE_PIECES)):
                    validmoves.append((moves[i][0], moves[i][1]))
            if((letter, number) in validmoves):
                return True
    return False

def isPawnAtFinalRank(lastpiece):
    if(lastpiece.__class__.__name__ == "Pawn" and (lastpiece.number == 1 and lastpiece.color == "black") or (lastpiece.number == 8 and lastpiece.color == "white")):
        return True
    return False

# Call at end of turn
def promotePawnAtEnd(BLACK_PIECES, WHITE_PIECES, changeTo):
    for x in range(len(BLACK_PIECES)):
        if(BLACK_PIECES[x].__class__.__name__ == "Pawn" and BLACK_PIECES[x].number == 1):
            BLACK_PIECES.pop(x)
            BLACK_PIECES.append(changeTo)
    for x in range(len(WHITE_PIECES)):
        if(WHITE_PIECES[x].__class__.__name__ == "Pawn" and WHITE_PIECES[x].number == 8):
            WHITE_PIECES.pop(x)
            WHITE_PIECES.append(changeTo)


def isValidforKing(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES): # TODO if castles - check to make sure in between square is not check
    if(movpiece.color == "white"):
        for x in range(len(WHITE_PIECES)):
            if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == number):
                return False
    else:
        for x in range(len(BLACK_PIECES)):
            if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == number):
                return False
    return LegalforKing(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES)