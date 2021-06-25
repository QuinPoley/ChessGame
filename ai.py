# Probably the worst chess ai of all time
import random
import LegalMove

def move(white, black, computerisblack, CAPTURED_BLACK_PIECES, CAPTURED_WHITE_PIECES, lastPiecetoMove, blackcheck, whitecheck, moveNumber):
    if(computerisblack):
        while True:
            piece = None
            if(blackcheck): # Am I in check?
                attackingpiece = LegalMove.getPieceAttackingKing("black", white, black, lastPiecetoMove)
                myking = LegalMove.getPosKing(black)
                blocks = LegalMove.listofblocks(attackingpiece, myking)
                if(len(attackingpiece) < 2):
                    blocks.append((attackingpiece[0].letter, attackingpiece[0].number)) # Capture the piece
                allowedindexlist = LegalMove.listofPiecesCapableOfBlock(blocks, black)
                if(random.randint(0, 1) == 1): # Coin flip because sometimes the king cant move when in check and it has to be blocked
                    piece = myking
                else:
                    index = random.randint(0, len(allowedindexlist)-1) # Attempted Piece to move
                    pieceindex = allowedindexlist[index]
                    piece = black[pieceindex]
                # Select king or a piece that can block
            else:
                if(moveNumber <= 2):      # PieceAT to 
                    kingsPawn = [(5,7), (5,5), (2,8), (3,6)]
                    QueensPawn = [(4,7), (4,5), (5,7), (5,6)]
                    Sicilian = [(3,7), (3,5), (4,7), (4,6)]
                    French = [(5,7), (5,6), (4,7), (4,5)] 
                    CaroKann = [(3,7), (3,6), (4,7), (4,5)]
                    listofOpenings = []
                    listofOpenings.append(kingsPawn)
                    listofOpenings.append(QueensPawn)
                    listofOpenings.append(Sicilian)
                    listofOpenings.append(French)
                    listofOpenings.append(CaroKann)
                    whichone = random.randint(0, len(listofOpenings)-1)

                    piece = LegalMove.getPieceAtSquare(listofOpenings[whichone][((moveNumber-1)*2)][0], listofOpenings[whichone][((moveNumber-1)*2)][1], black)
                    return [piece, listofOpenings[whichone][1+((moveNumber-1)*2)][0], listofOpenings[whichone][1+((moveNumber-1)*2)][1]]
                else:
                    index = random.randint(0, len(black)-1) # Attempted Piece to move
                    piece = black[index]
                    attmoves = piece.returnLegalMoves()
            
            if((len(attmoves) > 0)):
                wasJust = piece.letter, piece.number
                move = 0, 0
                if(blackcheck):
                    index = random.randint(0, len(blocks)-1)
                    move = blocks[index]
                    if(LegalMove.isValid(move[0], move[1], piece, black, white, lastPiecetoMove, blackcheck, whitecheck)):
                        #if(not LegalMove.causesCheck("black", black, white)):
                        print(piece.color + piece.__class__.__name__ + " @"+chr(96+wasJust[0])+","+str(wasJust[1])+" to "+ chr(96+move[0])+","+str(move[1]))
                        return [piece, move[0], move[1]]
                else:
                    move = random.randint(0, len(attmoves)-1)
                    if(LegalMove.isValid(attmoves[move][0], attmoves[move][1], piece, black, white, lastPiecetoMove, blackcheck, whitecheck)):
                        if(not LegalMove.causesCheck("black", black, white)):
                            print(piece.color + piece.__class__.__name__ + " @"+chr(96+wasJust[0])+","+str(wasJust[1])+" to "+ chr(96+attmoves[move][0])+","+str(attmoves[move][1]))
                            return [piece, attmoves[move][0], attmoves[move][1]]
        # Selected Piece had no moves, try again
# Randomly select piece, then if it has a valid move randomly select one of those