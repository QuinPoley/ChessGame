class Piece:
    def __init__(self, color, letter, number):
        self.position = letter, number
        self.letter = letter
        self.number = number
        self.color = color
        self.hasMoved = False

    def returnLegalMoves():
        return None
    
    def move(self, letter, number):
        firstmove = False
        if(not self.hasMoved):
            self.hasMoved = True
            firstmove = True
        self.letter = letter
        self.number = number
        return firstmove
    
    def returnHasMoved(self):
        return self.hasMoved


class Pawn(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)
    
    def returnLegalMoves(self):
        legalmoves = []
        if (self.color == "white"):
            #it can only move up that column, or capture in adjacent columns.
            legalmoves.append((self.letter, (self.number+1)))
            legalmoves.append(((self.letter+1), (self.number+1)))
            legalmoves.append(((self.letter-1), (self.number+1)))
            if(self.hasMoved == False):
                legalmoves.append((self.letter, (self.number+2)))
        else:
            legalmoves.append((self.letter, (self.number-1)))
            legalmoves.append(((self.letter+1), (self.number-1)))
            legalmoves.append(((self.letter-1), (self.number-1)))
            if(self.hasMoved == False):
                legalmoves.append((self.letter, (self.number-2)))
        return legalmoves # Giving all possible moves now, if piece can capture we check for that later
    
    def __str__(self):
        return self.color + " pawn @ " + chr(96+self.letter) +","+ self.number.__str__() # 96 Because the letter a is 97, and letter is 1 indexed

        

class King(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves(self):
        legalmoves = []

            #it doesnt matter if we include moves off board because the only clicks registered are on the board
        if(self.letter > 1):
            legalmoves.append(((self.letter-1), self.number))
            if(self.number > 1):
                legalmoves.append(((self.letter-1), (self.number-1)))
            if(self.number < 8):
                legalmoves.append(((self.letter-1), (self.number+1)))
        if(self.letter < 8):
            legalmoves.append(((self.letter+1), self.number))
            if(self.number > 1):
                legalmoves.append(((self.letter+1), (self.number-1)))
            if(self.number < 8):
                legalmoves.append(((self.letter+1), (self.number+1)))      
        if(self.number > 1):
            legalmoves.append((self.letter, (self.number-1)))
        if(self.number < 8):
            legalmoves.append((self.letter, (self.number+1)))
        
        if(self.hasMoved == False):
            legalmoves.append(((self.letter+2), self.number)) # Castle
            legalmoves.append(((self.letter-2), self.number))
        return legalmoves

    def __str__(self):
        return self.color + " King @ " + chr(96+self.letter) +","+ self.number.__str__()



        

class Queen(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves(self):
        legalmoves = []
        howFar = 9-self.letter if 9-self.letter < 9-self.number else 9-self.number #9?
        for x in range(1, howFar):
            legalmoves.append(((self.letter+x), (self.number+x)))# Diag Fwd Right
        
        howFar = self.letter if self.letter < 9-self.number else 9-self.number
        for x in range(1, howFar):
            legalmoves.append(((self.letter-x), (self.number+x)))# Diag Fwd Left
        
        howFar = 9-self.letter if 9-self.letter < self.number else self.number
        for x in range(1, howFar):
            legalmoves.append(((self.letter+x), (self.number-x)))# Diag Back Right

        howFar = self.letter if self.letter < self.number else self.number
        for x in range(1, howFar):
            legalmoves.append(((self.letter-x), (self.number-x)))# Diag Back Left

        for x in range((self.letter+1), 9):
            legalmoves.append((x, self.number))
        
        for x in range(1, self.letter):
            legalmoves.append((x, self.number))
        
        for x in range((self.number+1), 9):
            legalmoves.append((self.letter, x))
        
        for x in range(1, self.number):
            legalmoves.append((self.letter, x))
        return legalmoves
    
    def __str__(self):
        return self.color + " Queen @ " + chr(96+self.letter) +","+ self.number.__str__()


        

class Bishop(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves(self):
        legalmoves = []
        howFar = 9-self.letter if 9-self.letter < 9-self.number else 9-self.number #9?
        for x in range(1, howFar):
            legalmoves.append(((self.letter+x), (self.number+x)))# Diag Fwd Right
        
        howFar = self.letter if self.letter < 9-self.number else 9-self.number
        for x in range(1, howFar):
            legalmoves.append(((self.letter-x), (self.number+x)))# Diag Fwd Left
        
        howFar = 9-self.letter if 9-self.letter < self.number else self.number
        for x in range(1, howFar):
            legalmoves.append(((self.letter+x), (self.number-x)))# Diag Back Right

        howFar = self.letter if self.letter < self.number else self.number
        for x in range(1, howFar):
            legalmoves.append(((self.letter-x), (self.number-x)))# Diag Back Left
        
        return legalmoves
    
    def __str__(self):
        return self.color + " Bishop @ " + chr(96+self.letter) +","+ self.number.__str__()



        

class Knight(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)
    
    def returnLegalMoves(self):
        legalmoves = []
        # This one is trickiest, +1 and the other is +2
        if(self.letter > 1):
            if(self.number < 7):
                legalmoves.append(((self.letter-1), (self.number+2)))
            if(self.number > 2):
                legalmoves.append(((self.letter-1), (self.number-2)))
        if(self.letter < 8):
            if(self.number < 7):
                legalmoves.append(((self.letter+1), (self.number+2)))
            if(self.number > 2):
                legalmoves.append(((self.letter+1), (self.number-2)))
        if(self.letter < 7):
            if(self.number > 1):
                legalmoves.append(((self.letter+2), (self.number-1)))
            if(self.number < 8):
                legalmoves.append(((self.letter+2), (self.number+1)))
        if(self.letter > 2):
            if(self.number < 8):
                legalmoves.append(((self.letter-2), (self.number+1)))
            if(self.number > 1):
                legalmoves.append(((self.letter-2), (self.number-1)))
        return legalmoves
    
    def __str__(self):
        return self.color + "Knight @" + chr(96+self.letter) +","+ self.number.__str__()



        

class Rook(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves(self):
        legalmoves = []

        for x in range((self.letter+1), 9):
            legalmoves.append((x, self.number))
        
        for x in range(1, self.letter):
            legalmoves.append((x, self.number))
        
        for x in range((self.number+1), 9):
            legalmoves.append((self.letter, x))
        
        for x in range(1, self.number):
            legalmoves.append((self.letter, x))
        return legalmoves
    
    def __str__(self):
        return self.color + "Rook @" + chr(96+self.letter) +","+ self.number.__str__()
