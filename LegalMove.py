def LegalforPawn(letter, number, movpiece, BLACK_PIECES, WHITE_PIECES, lastpiece):
    # DIAGONAL MOVE CHECK
    if((letter < 1 or letter > 8) or (number < 1 or number > 8)):
        return False
    if(movpiece.color == "white" and movpiece.letter != letter): # white pawn moving diagonally
            for x in range(len(BLACK_PIECES)):
                if(BLACK_PIECES[x].letter == letter and BLACK_PIECES[x].number == number):
                    return True
                elif(lastpiece.__class__.__name__ == "Pawn"): # En passant check
                    if(lastpiece.letter == letter and lastpiece.number == (number-1)): # Valid
                        return True
            return False # Not a capture, hence not valid
    elif(movpiece.color == "black" and movpiece.letter != letter):
            for x in range(len(WHITE_PIECES)):
                if(WHITE_PIECES[x].letter == letter and WHITE_PIECES[x].number == number):
                    return True
                elif(lastpiece.__class__.__name__ == "Pawn"): # En passant
                    if(lastpiece.letter == letter and lastpiece.number == (number+1)):
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
    return True

def listofblocks(att, king, BLACK_PIECES, WHITE_PIECES):
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