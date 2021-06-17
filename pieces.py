class Piece:
    def __init__(self, color, letter, number):
        self.position = letter, number
        self.letter = letter
        self.number = number
        self.color = color
        self.captured = False

    def returnLegalMoves():
        return None


class Pawn(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)
    
    def returnLegalMoves(self):
        legalmoves = []
        if (self.color == "white"):
            #it can only move up that column, or capture in adjacent columns.
            legalmoves.append((self.letter, (self.number+1)))
            legalmoves.append((self.letter, (self.number+2)))
            legalmoves.append(((self.letter+1), (self.number+1)))
            legalmoves.append(((self.letter-1), (self.number+1)))
        else:
            legalmoves.append((self.letter, (self.number-1)))
            legalmoves.append((self.letter, (self.number-2)))
            legalmoves.append(((self.letter+1), (self.number-1)))
            legalmoves.append(((self.letter-1), (self.number-1)))
        return legalmoves # Giving all possible moves now, if piece can capture or is first move we check for that later
    
    def __str__(self):
        return self.color + " pawn @ " + chr(96+self.letter) +","+ self.number.__str__() # 96 Because the letter a is 97, and letter is 1 indexed

        

class King(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves(self):
        legalmoves = []

            #it doesnt matter if we include moves off board because the only clicks registered are on the board
        legalmoves.append((self.letter, (self.number+1)))
        legalmoves.append(((self.letter+1), (self.number+1)))
        legalmoves.append(((self.letter+1), self.number))
        legalmoves.append(((self.letter-1), (self.number+1)))
        legalmoves.append(((self.letter+1), (self.number-1)))
        legalmoves.append(((self.letter-1), (self.number-1)))
        legalmoves.append(((self.letter-1), self.number))
        legalmoves.append((self.letter, (self.number-1)))
        #legalmoves.append(((self.letter+2), self.number))
        #legalmoves.append(((self.letter-2), self.number))
        
        return legalmoves
    
    def __str__(self):
        return self.color + " King @ " + chr(96+self.letter) +","+ self.number.__str__()



        

class Queen(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves(self):
        legalmoves = []
        for x in range(1, 8):
            legalmoves.append(((self.letter+x), (self.number+x))) # Diag Fwd Right
            legalmoves.append(((self.letter-x), (self.number+x))) # Diag Fwd Left
            legalmoves.append(((self.letter+x), (self.number-x))) # Diag Back Right
            legalmoves.append(((self.letter-x), (self.number-x))) # Diag Back Left
            legalmoves.append(((self.letter), (self.number+x))) # Direct Fwd
            legalmoves.append(((self.letter+x), (self.number))) # Direct Right
            legalmoves.append(((self.letter-x), (self.number))) # Direct Left
            legalmoves.append(((self.letter), (self.number-x))) # Direct Back
        return legalmoves
    
    def __str__(self):
        return self.color + " Queen @ " + chr(96+self.letter) +","+ self.number.__str__()


        

class Bishop(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves(self):
        legalmoves = []
        for x in range(1, 8):
            legalmoves.append(((self.letter+x), (self.number+x))) # Diag Fwd Right
            legalmoves.append(((self.letter-x), (self.number+x))) # Diag Fwd Left
            legalmoves.append(((self.letter+x), (self.number-x))) # Diag Back Right
            legalmoves.append(((self.letter-x), (self.number-x))) # Diag Back Left
        return legalmoves
    
    def __str__(self):
        return self.color + " Bishop @ " + chr(96+self.letter) +","+ self.number.__str__()



        

class Knight(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)
    
    def returnLegalMoves(self):
        legalmoves = []
        # This one is trickiest, +1 and the other is +2
        legalmoves.append(((self.letter-1), (self.number+2)))
        legalmoves.append(((self.letter-1), (self.number-2)))
        legalmoves.append(((self.letter+1), (self.number+2)))
        legalmoves.append(((self.letter+1), (self.number-2)))
        legalmoves.append(((self.letter+2), (self.number-1)))
        legalmoves.append(((self.letter+2), (self.number+1)))
        legalmoves.append(((self.letter-2), (self.number+1)))
        legalmoves.append(((self.letter-2), (self.number-1)))
        return legalmoves
    
    def __str__(self):
        return self.color + "Knight @" + chr(96+self.letter) +","+ self.number.__str__()



        

class Rook(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves(self):
        legalmoves = []
        for x in range(1, 8):
            legalmoves.append(((self.letter), (self.number+x))) # Direct Fwd
            legalmoves.append(((self.letter+x), (self.number))) # Direct Right
            legalmoves.append(((self.letter-x), (self.number))) # Direct Left
            legalmoves.append(((self.letter), (self.number-x))) # Direct Back
        return legalmoves
    
    def __str__(self):
        return self.color + "Rook @" + chr(96+self.letter) +","+ self.number.__str__()


