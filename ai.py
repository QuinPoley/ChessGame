# Probably the worst chess ai of all time
import random
import LegalMove
import Engine

class ComputerOpponent:
    def __init__(self):
        self.moveNumber = 0
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
        self.selectedopening = random.randint(0, len(listofOpenings)-1)
        self.listofOpenings = listofOpenings


    def move(self, white, black, computerisblack, CAPTURED_BLACK_PIECES, CAPTURED_WHITE_PIECES, lastPiecetoMove, blackcheck, whitecheck):
        if(computerisblack):
            self.moveNumber += 1
            blackAttemptedMove = black.copy()
            BestMove = []
            while True:
                piece = None
                if(blackcheck): # Am I in check?
                    attackingpiece = LegalMove.getPieceAttackingKing("black", white, blackAttemptedMove, lastPiecetoMove)
                    myking = LegalMove.getPosKing(blackAttemptedMove)
                    blocks = LegalMove.listofblocks(attackingpiece, myking)
                    if(len(attackingpiece) < 2):
                        blocks.append((attackingpiece[0].letter, attackingpiece[0].number)) # Capture the piece
                    allowedindexlist = LegalMove.listofPiecesCapableOfBlock(blocks, black)
                    if(len(allowedindexlist) == 0): # Cannot be blocked or captured
                        piece = myking
                        blocks = piece.returnLegalMoves() # King moving outside of legal moves = bad
                    else:
                        index = random.randint(0, len(allowedindexlist)-1) # Attempted Piece to move
                        pieceindex = allowedindexlist[index]
                        piece = blackAttemptedMove[pieceindex]
                    # Select king or a piece that can block
                else:
                    if(self.moveNumber <= 2):      # PieceAT to 
                        piece = LegalMove.getPieceAtSquare(self.listofOpenings[self.selectedopening][((self.moveNumber-1)*2)][0], self.listofOpenings[self.selectedopening][((self.moveNumber-1)*2)][1], blackAttemptedMove)
                        return [piece, self.listofOpenings[self.selectedopening][1+((self.moveNumber-1)*2)][0], self.listofOpenings[self.selectedopening][1+((self.moveNumber-1)*2)][1]]
                    else:
                        file = open("log.txt", "w+")
                        WhiteMaterialLeft= 140
                        RatioOfSquaresControlled = 100.0
                         # the first is the piece, the second is where to
                        for x in range(len(blackAttemptedMove)):
                            legalmoves = blackAttemptedMove[x].returnLegalMoves()
                            wasJust = blackAttemptedMove[x].letter, blackAttemptedMove[x].number
                            for i in range(len(legalmoves)):
                                if(LegalMove.isValid(legalmoves[i][0], legalmoves[i][1], blackAttemptedMove[x], black, white, lastPiecetoMove, blackcheck, whitecheck)):
                                    blackAttemptedMove[x].move(legalmoves[i][0], legalmoves[i][1])
                                    values = Engine.Eval(white, blackAttemptedMove)
                                    file.write(str(blackAttemptedMove[x]) + " "+ str(legalmoves[i][0]) + ","+  str(legalmoves[i][1]) + " "+ str(values[0]) + " " + str(WhiteMaterialLeft) + " " + str(values[2]) + " " +  str(RatioOfSquaresControlled)+"\n")
                                    print(values[0] >= WhiteMaterialLeft)
                                    print(values[2] <= RatioOfSquaresControlled)
                                    if(values[0] >= WhiteMaterialLeft and values[2] <= RatioOfSquaresControlled): # Check if its the best move so far
                                        BestMove = [(blackAttemptedMove[x].letter, blackAttemptedMove[x].number), wasJust]
                                        WhiteMaterialLeft = values[0]
                                        RatioOfSquaresControlled = values[2]
                                    blackAttemptedMove[x].letter = wasJust[0]
                                    blackAttemptedMove[x].number = wasJust[1]  # Put it back
                        file.close()
                        if(len(BestMove) == 0):
                            moves = []
                            while (len(moves) == 0):
                                randindex = random.randint(0, len(black)-1)
                                moves = black[randindex].returnLegalMoves()
                            BestMove = [moves[0], (black[randindex].letter, black[randindex].number)]
                        piece = LegalMove.getPieceAtSquare(BestMove[1][0], BestMove[1][1], blackAttemptedMove)


                wasJust = piece.letter, piece.number
                move = 0, 0
                if(blackcheck):
                    index = random.randint(0, len(blocks)-1)
                    move = blocks[index]
                    if(LegalMove.isValid(move[0], move[1], piece, black, white, lastPiecetoMove, blackcheck, whitecheck)):
                        piece.move(move[0], move[1])
                        if(not LegalMove.causesCheck("black", blackAttemptedMove, white)): # No moving into check even to get out of it
                            piece = LegalMove.getPieceAtSquare(move[0], move[1], black) # get out of right list
                            print(piece.color + piece.__class__.__name__ + " @"+chr(96+wasJust[0])+","+str(wasJust[1])+" to "+ chr(96+move[0])+","+str(move[1]))
                            return [piece, move[0], move[1]]
                        else:
                            piece.letter, piece.number = wasJust
                else:
                    if(LegalMove.isValid(BestMove[0][0], BestMove[0][1], piece, black, white, lastPiecetoMove, blackcheck, whitecheck)):
                        piece.move(BestMove[0][0], BestMove[0][1])
                        if(not LegalMove.causesCheck("black", blackAttemptedMove, white)): # No moving into check
                            piece.letter, piece.number = wasJust
                            piece = LegalMove.getPieceAtSquare(BestMove[1][0], BestMove[1][1], black) # get out of right list
                            print(piece.color + piece.__class__.__name__ + " @"+chr(96+wasJust[0])+","+str(wasJust[1])+" to "+ chr(96+BestMove[0][0])+","+str(BestMove[0][1]))
                            return [piece, BestMove[0][0], BestMove[0][1]]    
                        else:
                            piece.letter, piece.number = wasJust
        # Selected Piece had no moves, try again
# Randomly select piece, then if it has a valid move randomly select one of those