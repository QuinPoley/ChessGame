# Probably the worst chess ai of all time
import random
import LegalMove

def move(white, black, computerisblack, CAPTURED_BLACK_PIECES, CAPTURED_WHITE_PIECES, lastPiecetoMove):
    if(computerisblack):
        while True:
            index = random.randint(0, len(black)-1) # Attempted Piece to move
            piece = black[index]
            attmoves = piece.returnLegalMoves()
            legalmoves = []
            piecethere = False
            for x in range(len(attmoves)):
                for i in range(len(black)):
                    if(attmoves[x][0] == black[i].letter and attmoves[x][1] == black[i].number):
                        piecethere = True
                if(piece.__class__.__name__ == "Pawn" and not piecethere):
                    if(LegalMove.LegalforPawnCheck(attmoves[x][0], attmoves[x][1], piece, black, white)):
                        legalmoves.append((attmoves[x][0], attmoves[x][1]))
                elif(piece.__class__.__name__ == "Queen" and not piecethere):
                    if(LegalMove.LegalforQueen(attmoves[x][0], attmoves[x][1], piece, black, white)):
                        legalmoves.append((attmoves[x][0], attmoves[x][1]))
                elif(piece.__class__.__name__ == "Rook" and not piecethere):
                    if(LegalMove.LegalforRook(attmoves[x][0], attmoves[x][1], piece, black, white)):
                        legalmoves.append((attmoves[x][0], attmoves[x][1]))
                elif(piece.__class__.__name__ == "Bishop" and not piecethere):
                    if(LegalMove.LegalforBishop(attmoves[x][0], attmoves[x][1], piece, black, white)):
                        legalmoves.append((attmoves[x][0], attmoves[x][1]))
                elif(piece.__class__.__name__ == "Knight" and not piecethere):
                    if(LegalMove.LegalforKnight(attmoves[x][0], attmoves[x][1], piece, black, white)):
                        legalmoves.append((attmoves[x][0], attmoves[x][1]))
                elif(piece.__class__.__name__ == "King" and not piecethere):
                    if(LegalMove.LegalforKing(attmoves[x][0], attmoves[x][1], piece, black, white)):
                        legalmoves.append((attmoves[x][0], attmoves[x][1]))
            
            if((len(legalmoves) > 0)):
                wasJust = piece.letter, piece.number
                move = random.randint(0, len(legalmoves)-1)
                LegalMove.isCapture(attmoves[move][0], attmoves[move][1], piece, black, white, CAPTURED_BLACK_PIECES, CAPTURED_WHITE_PIECES, lastPiecetoMove)
                piece.move(attmoves[move][0], attmoves[move][1])
                print(piece.color + piece.__class__.__name__ + " @"+chr(96+wasJust[0])+","+str(wasJust[1])+" to "+ chr(96+attmoves[move][0])+","+str(attmoves[move][1]))
                return True
        # Selected Piece had no moves, try again
# Randomly select piece, then if it has a valid move randomly select one of those