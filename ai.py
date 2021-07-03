# Probably the worst chess ai of all time
import random
from typing import ByteString
import LegalMove
import Engine
import copy

class ComputerOpponent:
    def __init__(self):
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

    def getOutOfCheck(self, white, black, blackcheck, whitecheck, prev):
        while True:
            attackingpiece = LegalMove.getPieceAttackingKing("black", white, black, prev)
            myking = LegalMove.getPosKing(black)
            blocks = LegalMove.listofblocks(attackingpiece, myking)
            if(len(attackingpiece) < 2):
                blocks.append((attackingpiece[0].letter, attackingpiece[0].number)) # Capture the piece
            allowedindexlist = LegalMove.listofPiecesCapableOfBlock(blocks, black)
            if(len(allowedindexlist) == 0): # Cannot be blocked or captured
                piece = myking
                blocks = piece.returnLegalMoves() # King moving outside of legal moves = bad
            else:
                # We are blocking check, might as well do it with the lowest value piece
                index = -1
                CurrentValueBlock = 90
                for x in range(len(allowedindexlist)):
                    if(black[allowedindexlist[x]].value < CurrentValueBlock):
                        index = x
                        CurrentValueBlock = black[allowedindexlist[x]].value

                pieceindex = allowedindexlist[index]
                piece = black[pieceindex]
            index = random.randint(0, len(blocks)-1)
            move = blocks[index]

            if(LegalMove.isValid(move[0], move[1], piece, black, white, prev, blackcheck, whitecheck) and not LegalMove.isCheckAfterMove(move[0], move[1], piece, black, white)):
                piece.move(move[0], move[1])
                return [piece, move[0], move[1]]

    def EvaluateBoard(self, white, black):
        # Take the engine eval and simplfy it to one number how good is it for me
        WhiteMat, BlackMat, Control, WhiteSafe, BlackSafe = Engine.Eval(white, black)
        BoardState = ((BlackMat - WhiteMat) * 3) + Control + ((BlackSafe - WhiteSafe) * 2) - 1  # Default 0 More is great, less is bad
        return BoardState

    def FindBestMove(self, white, black, prev, BC, WC):
        CopyWhite = copy.deepcopy(white)
        CopyBlack = copy.deepcopy(black)
        BestState = -1000 # Real bad for us
        BestMoveForBlack = []
        BestMoveForWhite = []
        for x in range(len(CopyBlack)):
            moves = CopyBlack[x].returnLegalMoves()
            for i in range(len(moves)):
                if(LegalMove.isValid(moves[i][0], moves[i][1], CopyBlack[x], CopyBlack, CopyWhite, prev, BC, WC) and not LegalMove.isCheckAfterMove(moves[i][0], moves[i][1], CopyBlack[x], CopyBlack, CopyWhite)):
                    wasJust = CopyBlack[x].letter, CopyBlack[x].number
                    CopyBlack[x].move(moves[i][0], moves[i][1])
                    value = self.EvaluateBoard(CopyWhite, CopyBlack)
                    if(value > BestState):
                        BestMoveForBlack = [CopyBlack[x], moves[i][0], moves[i][1]]
                        BestState = value
                        for j in range(len(CopyWhite)):
                            wmoves = CopyWhite[j].returnLegalMoves()
                            for k in range(len(wmoves)):
                                if(LegalMove.isValid(wmoves[k][0], wmoves[k][1], CopyWhite[j], CopyBlack, CopyWhite, prev, BC, WC) and not LegalMove.isCheckAfterMove(wmoves[k][0], wmoves[k][1], CopyBlack[x], CopyBlack, CopyWhite)):
                                    previously = CopyWhite[j].letter, CopyWhite[j].number
                                    CopyWhite[x].move(wmoves[k][0], wmoves[k][1])
                                    newvalue = self.EvaluateBoard(CopyWhite, CopyBlack)
                                    if(newvalue < BestState):
                                        BestMoveForWhite = [CopyWhite[j], wmoves[k][0], wmoves[k][1]]
                                        BestState = newvalue
                                    CopyWhite[j].letter, CopyWhite[j].number = previously
                    CopyBlack[x].letter, CopyBlack[x].number = wasJust

        print(BestMoveForBlack[0].__str__()+ " " +str(BestMoveForBlack[1])+ " " +str(BestMoveForBlack[2]))
        print(BestMoveForWhite[0].__str__()+ " " +str(BestMoveForWhite[1])+ " " +str(BestMoveForWhite[2]))
        return BestMoveForBlack

    def move(self, white, black, computerisblack, lastPiecetoMove, blackcheck, whitecheck, movenumber):
        if(computerisblack):
            while True:
                piece = None
                if(blackcheck): # Am I in check?
                     return self.getOutOfCheck(white, black, blackcheck, whitecheck, lastPiecetoMove)
                else:
                    if(movenumber <= 2):      # Use the openings I gave it
                        piece = LegalMove.getPieceAtSquare(self.listofOpenings[self.selectedopening][((movenumber-1)*2)][0], self.listofOpenings[self.selectedopening][((movenumber-1)*2)][1], black)
                        return [piece, self.listofOpenings[self.selectedopening][1+((movenumber-1)*2)][0], self.listofOpenings[self.selectedopening][1+((movenumber-1)*2)][1]]
                    else: # Try to use the engine I wrote to find the best move
                        return self.FindBestMove(white, black, lastPiecetoMove, blackcheck, whitecheck)
