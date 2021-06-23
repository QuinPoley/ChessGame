# Evaluate Board State
import LegalMove

# Maybe eventually who's turn
def Eval(white, black):
    #ValuesOfPieces
    KingValue = 100
    QueenValue = 10
    RookValue = 5
    BishopValue = 3
    KnightValue = 3
    PawnValue = 1

    WhiteMaterial = 0
    BlackMaterial = 0
    for x in range(len(white)):
        if(white[x].__class__.__name__ == "King"):
            WhiteMaterial += KingValue
        elif(white[x].__class__.__name__ == "Queen"):
            WhiteMaterial += QueenValue
        elif(white[x].__class__.__name__ == "Rook"):
            WhiteMaterial += RookValue
        elif(white[x].__class__.__name__ == "Bishop"):
            WhiteMaterial += BishopValue
        elif(white[x].__class__.__name__ == "Knight"):
            WhiteMaterial += KnightValue
        elif(white[x].__class__.__name__ == "Pawn"):
            WhiteMaterial += PawnValue

    for x in range(len(black)):
        if(black[x].__class__.__name__ == "King"):
            BlackMaterial += KingValue
        elif(black[x].__class__.__name__ == "Queen"):
            BlackMaterial += QueenValue
        elif(black[x].__class__.__name__ == "Rook"):
            BlackMaterial += RookValue
        elif(black[x].__class__.__name__ == "Bishop"):
            BlackMaterial += BishopValue
        elif(black[x].__class__.__name__ == "Knight"):
            BlackMaterial += KnightValue
        elif(black[x].__class__.__name__ == "Pawn"):
            BlackMaterial += PawnValue

    listWhite = []
    listBlack = []
    for x in range(len(white)):
        moves = white[x].returnLegalMoves()
        if(white[x].__class__.__name__ == "King"):
            for i in range(len(moves)):
                if(not moves[i] in listWhite and LegalMove.LegalforKing(moves[i][0], moves[i][1], white[x], black, white)):
                    listWhite.append((moves[i][0], moves[i][1]))  
        elif(white[x].__class__.__name__ == "Queen"):
            for i in range(len(moves)):
                if(not moves[i] in listWhite and LegalMove.LegalforQueen(moves[i][0], moves[i][1], white[x], black, white)):
                    listWhite.append((moves[i][0], moves[i][1]))
        elif(white[x].__class__.__name__ == "Rook"):
            for i in range(len(moves)):
                if(not moves[i] in listWhite and LegalMove.LegalforRook(moves[i][0], moves[i][1], white[x], black, white)):
                    listWhite.append((moves[i][0], moves[i][1]))
        elif(white[x].__class__.__name__ == "Bishop"):
            for i in range(len(moves)):
                if(not moves[i] in listWhite and LegalMove.LegalforBishop(moves[i][0], moves[i][1], white[x], black, white)):
                    listWhite.append((moves[i][0], moves[i][1]))
        elif(white[x].__class__.__name__ == "Knight"):
            for i in range(len(moves)):
                if(not moves[i] in listWhite and LegalMove.LegalforKnight(moves[i][0], moves[i][1], white[x], black, white)):
                    listWhite.append((moves[i][0], moves[i][1]))
        elif(white[x].__class__.__name__ == "Pawn"):
            for i in range(len(moves)):
                if(not moves[i] in listWhite and LegalMove.LegalforPawnCheck(moves[i][0], moves[i][1], white[x], black, white)):
                    listWhite.append((moves[i][0], moves[i][1]))
    
    for x in range(len(black)):
        moves = black[x].returnLegalMoves()
        if(black[x].__class__.__name__ == "King"):
            for i in range(len(moves)):
                if(not moves[i] in listBlack and LegalMove.LegalforKing(moves[i][0], moves[i][1], white[x], black, white)):
                    listBlack.append((moves[i][0], moves[i][1]))  
        elif(black[x].__class__.__name__ == "Queen"):
            for i in range(len(moves)):
                if(not moves[i] in listBlack and LegalMove.LegalforQueen(moves[i][0], moves[i][1], white[x], black, white)):
                    listBlack.append((moves[i][0], moves[i][1]))
        elif(black[x].__class__.__name__ == "Rook"):
            for i in range(len(moves)):
                if(not moves[i] in listBlack and LegalMove.LegalforRook(moves[i][0], moves[i][1], white[x], black, white)):
                    listBlack.append((moves[i][0], moves[i][1]))
        elif(black[x].__class__.__name__ == "Bishop"):
            for i in range(len(moves)):
                if(not moves[i] in listBlack and LegalMove.LegalforBishop(moves[i][0], moves[i][1], white[x], black, white)):
                    listBlack.append((moves[i][0], moves[i][1]))
        elif(black[x].__class__.__name__ == "Knight"):
            for i in range(len(moves)):
                if(not moves[i] in listBlack and LegalMove.LegalforKnight(moves[i][0], moves[i][1], white[x], black, white)):
                    listBlack.append((moves[i][0], moves[i][1]))
        elif(black[x].__class__.__name__ == "Pawn"):
            for i in range(len(moves)):
                if(not moves[i] in listBlack and LegalMove.LegalforPawnCheck(moves[i][0], moves[i][1], white[x], black, white)):
                    listBlack.append((moves[i][0], moves[i][1]))
        # Do a ratio of who has control ie can capture over more squares

    
    ratioOfControlledSquares = float(len(listWhite)) / float(len(listBlack))
    # Who's king is safer?
    WhiteSafety = 10.0
    BlackSafety = 10.0
    WhiteKing = LegalMove.getPosKing(white)
    BlackKing = LegalMove.getPosKing(black)
    if((WhiteKing.letter, WhiteKing.number) in listBlack): # White is in check
        WhiteSafety -= 5.0 # 5 so we can later subtract and determine how close to checkmate
    WhiteMoves = WhiteKing.returnLegalMoves()
    LegalWhiteKing = []
    for x in range(len(WhiteMoves)):
        if(LegalMove.isValidforKing(WhiteMoves[x][0],  WhiteMoves[x][1], WhiteKing, black, white)):
            LegalWhiteKing.append((WhiteMoves[x][0], WhiteMoves[x][1]))
    
    if(len(LegalWhiteKing) != 0):
        for x in range(len(LegalWhiteKing)):
            if((LegalWhiteKing[x][0], LegalWhiteKing[x][1]) in listWhite):
                BlackSafety -= (5.0 / len(LegalWhiteKing)) # get to 0 for checkmate

    if((BlackKing.letter, BlackKing.number) in listWhite): # White is in check
        BlackSafety -= 5.0 # 5 so we can later subtract and determine how close to checkmate
    BlackMoves = BlackKing.returnLegalMoves()
    LegalBlackKing = []
    for x in range(len(BlackMoves)):
        if(LegalMove.isValidforKing(BlackMoves[x][0],  BlackMoves[x][1], BlackKing, black, white)):
            LegalBlackKing.append((BlackMoves[x][0], BlackMoves[x][1]))
    if(len(LegalBlackKing) != 0):
        for x in range(len(LegalBlackKing)):
            if((LegalBlackKing[x][0], LegalBlackKing[x][1]) in listWhite):
                BlackSafety -= (5.0 / len(LegalBlackKing)) # get to 0 for checkmate

    return [WhiteMaterial, BlackMaterial, ratioOfControlledSquares, WhiteSafety, BlackSafety]
    

