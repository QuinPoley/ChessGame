import LegalMove
from pieces import *
# Agnostic of pygame, lets make the game

class GameOfChess():
    def __init__(self):
        self.White = []
        self.Black = []
        self.CapturedWhite = []
        self.CapturedBlack = []
        self.WhiteTurn = True
        self.MoveNumber = 0
        self.WhiteCheck = False
        self.BlackCheck = False
        self.CurrentlySelected = None
        self.PreviouslyMovingPiece = None
        self.Checkmate = False
        self.Winner = ""

        for x in range(1, 9): # Do all the pawns
            self.White.append(Pawn("white", x, 2)) # X is really the letter but numbers work
            self.Black.append(Pawn("black", x, 7))
            if (x == 1 or x == 8):
                self.White.append(Rook("white", x, 1))
                self.Black.append(Rook("black", x, 8))
            elif(x == 2 or x == 7):
                self.White.append(Knight("white", x, 1))
                self.Black.append(Knight("black", x, 8))
            elif(x == 3 or x == 6):
                self.White.append(Bishop("white", x, 1))
                self.Black.append(Bishop("black", x, 8))
            elif(x == 4):
                self.White.append(Queen("white", x, 1))
                self.Black.append(Queen("black", x, 8))
            else:
                self.White.append(King("white", x, 1))
                self.Black.append(King("black", x, 8))

    def LocateMouseDown(self, pos):
        x, y = pos
        squareX = (x //100) + 1
        squareY = 8 - (y //100)
        return (squareX, squareY)

    def SelectPiece(self, pos):
        squarex, squarey = self.LocateMouseDown(pos)
        SelectedPiece = LegalMove.WrapperGetPieceAtSquare(squarex, squarey, self.White, self.Black)
        if(SelectedPiece == None):
            return
        if((SelectedPiece.color == "white" and self.WhiteTurn == False) or (SelectedPiece.color == "black" and self.WhiteTurn == True)):
            return

        self.CurrentlySelected = SelectedPiece # Okay, legal selection

    # Is the color in check?
    def Check(self, color):
        King = None
        if(color == "white"):
            King = LegalMove.getPosKing(self.White)
        else:
            King = LegalMove.getPosKing(self.Black)
        letter = King.letter
        number = King.number
    
        if(color == "white"): # is white in check?
            for x in range(len(self.Black)):
                moves = self.Black[x].returnLegalMoves()
                validmoves = []
                for i in range(len(moves)):
                    if(LegalMove.isSquareCapturable(moves[i][0], moves[i][1], self.Black[x], self.Black, self.White)): # Can this piece capture this square
                        validmoves.append((moves[i][0], moves[i][1]))
                if((letter, number) in validmoves):
                    return True       
        else: # is black in check?
            for x in range(len(self.White)):
                moves = self.White[x].returnLegalMoves()
                validmoves = []
                for i in range(len(moves)):
                    if(LegalMove.isSquareCapturable(moves[i][0], moves[i][1], self.White[x], self.Black, self.White)): # Can this piece capture this square
                        validmoves.append((moves[i][0], moves[i][1]))
                if((letter, number) in validmoves):
                    return True
        return False

    def isCheckMate(self, color):
        if(not self.Check(color)):
            return False
        King = None
        if(color == "white"):
            King = LegalMove.getPosKing(self.White)
        else:
            King = LegalMove.getPosKing(self.Black)
        moves = King.returnLegalMoves()
        for x in range(len(moves)):
            if(LegalMove.isValid(moves[x][0], moves[x][1], King, BLACK_PIECES, self.White, self.PreviouslyMovingPiece)):
                if(not isCheck(color, moves[x][0], moves[x][1])):
                    return False
        attackers = LegalMove.getPieceAttackingKing(color, self.White, BLACK_PIECES, self.PreviouslyMovingPiece)
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
                    else:
                        return False
        # King cannot move, and piece cannot be captured. Can it be blocked?
        isBlockable = LegalMove.listofblocks(attackers, King)
        if(color == "white"):
            for x in range(len(WHITE_PIECES)):
                moves = WHITE_PIECES[x].returnLegalMoves()
                validmoves = []
                for i in range(len(moves)):
                    if(LegalMove.isValid(moves[i][0], moves[i][1], WHITE_PIECES[x], BLACK_PIECES, WHITE_PIECES, lastPiecetoMove)):
                        validmoves.append((moves[i][0], moves[i][1]))
                for i in range(len(isBlockable)):
                    if(isBlockable[i] in validmoves): # There is a valid move that blocks the check
                        return False
        else:
            for x in range(len(BLACK_PIECES)):
                moves = BLACK_PIECES[x].returnLegalMoves()
                validmoves = []
                for i in range(len(moves)):
                    if(LegalMove.isValid(moves[i][0], moves[i][1], BLACK_PIECES[x], BLACK_PIECES, WHITE_PIECES, lastPiecetoMove)):
                        validmoves.append((moves[i][0], moves[i][1]))
                for i in range(len(isBlockable)):
                    if(isBlockable[i] in validmoves): # There is a valid move that blocks the check
                        return False
        # Now we have a list of possible blocks. Can we move there?
        #if(isBlockable):
        #    return False
        return True

    def Castle(self, color, istoRight):
        default = 1
        movingTo = 4
        if(istoRight):
            default = 8
            movingTo = 6
        if(color == "white"):
            for x in range(len(self.White)):
                if(self.White[x].number == 1 and self.White[x].letter == default):
                    self.White[x].letter = movingTo # Move Rook to other side
        else:
            for x in range(len(self.Black)):
                if(self.Black[x].number == 8 and self.Black[x].letter == default):
                    self.Black[x].letter = movingTo # Move Rook to other side

    def PromotePawns(self):
        if(LegalMove.isPawnAtFinalRank(self.PreviouslyMovingPiece)):
            Promotion = None
            if(self.PreviouslyMovingPiece.color == "white"):
                Promotion = LegalMove.getPieceAtSquare(self.PreviouslyMovingPiece.letter, self.PreviouslyMovingPiece.number, self.White)
                LegalMove.promotePawnAtEnd(self.White, Queen("", Promotion.letter, Promotion.number), "white")
            else:
                Promotion = LegalMove.getPieceAtSquare(self.PreviouslyMovingPiece.letter, self.PreviouslyMovingPiece.number, self.Black)
                LegalMove.promotePawnAtEnd(self.White, Queen("", Promotion.letter, Promotion.number), "white")

           

    # True if valid move completed
    # False otherwise
    def MovePiece(self, Piece, Location):
        if((self.WhiteTurn and Piece.color == "black") or (not self.WhiteTurn and Piece.color == "white") or Piece == None):
            return False # Not your turn or no piece
        
        self.WhiteCheck = self.Check("white")
        self.BlackCheck = self.Check("black")

        if((self.WhiteTurn and self.WhiteCheck) or (not self.WhiteTurn and self.BlackCheck)):
            print() # In check, lets limit moves to those that block or get out of check

        else: # Not in check
            if(LegalMove.isValid(Location[0], Location[1], Piece, self.Black, self.White, self.PreviouslyMovingPiece, self.BlackCheck, self.WhiteCheck) and not LegalMove.isCheckAfterMove(Location[0], Location[1], Piece, self.Black, self.White)): # Move Valid
                Piece.move(Location[0], Location[1]) # Because the move is valid, does not cause check, and we were not in check
                LegalMove.isCapture(Location[0], Location[1], Piece, self.Black, self.White, self.CapturedBlack, self.CapturedWhite, self.PreviouslyMovingPiece)
                # Eventually I want to remove the piece here, and iscapture should just return true or false
                #if(LegalMove.isCapture()):
                #    if(Piece.color == "white"):
                #        LegalMove.getPieceAtSquare(Location[0], Location[1])
                

        # IS IT CHECKMATE???
        color = "black" if self.WhiteTurn else "white" # Color not moving
        if(self.CheckMate(color)):
            self.Checkmate = True
            self.Winner = Piece.color

        self.WhiteCheck = self.Check("white")
        self.BlackCheck = self.Check("black")
        self.PreviouslyMovingPiece = Piece
        self.PromotePawns()
        self.WhiteTurn = False if self.WhiteTurn else True # Flip turn
        self.MoveNumber += 1
