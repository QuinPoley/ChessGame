# Probably the worst chess ai of all time
import random
import LegalMove

def move(white, black, computerisblack, CAPTURED_BLACK_PIECES, CAPTURED_WHITE_PIECES, lastPiecetoMove):
    if(computerisblack):
        while True:
            index = random.randint(0, len(black)-1) # Attempted Piece to move
            piece = black[index]
            attmoves = piece.returnLegalMoves()
            
            if((len(attmoves) > 0)):
                wasJust = piece.letter, piece.number
                move = random.randint(0, len(attmoves)-1)
                if(LegalMove.isValid(attmoves[move][0], attmoves[move][1], piece, black, white, lastPiecetoMove)):
                    if(not LegalMove.causesCheck("black", black, white)):
                        print(piece.color + piece.__class__.__name__ + " @"+chr(96+wasJust[0])+","+str(wasJust[1])+" to "+ chr(96+attmoves[move][0])+","+str(attmoves[move][1]))
                        return [piece, attmoves[move][0], attmoves[move][1]]
        # Selected Piece had no moves, try again
# Randomly select piece, then if it has a valid move randomly select one of those