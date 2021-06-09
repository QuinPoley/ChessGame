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
    
    def returnLegalMoves():
        if (super().color == "white"):
            #it can only move up that column, or capture in adjacent columns.
            print()
        else:
            #it can only move down
            print()
    
    def __str__(self):
        return self.color + " pawn @ " + chr(97+self.letter) +","+ self.number.__str__()

        

class King(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves():
        if (super().color == "white"):
            #it can only move up that column, or capture in adjacent columns.
            print()
        else:
            #it can only move down
            print()
    
    def __str__(self):
        return self.color + " King @ " + chr(97+self.letter) +","+ self.number.__str__()



        

class Queen(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves():
        if (super().color == "white"):
            #it can only move up that column, or capture in adjacent columns.
            print()
        else:
            #it can only move down
            print()
    
    def __str__(self):
        return self.color + " Queen @ " + chr(97+self.letter) +","+ self.number.__str__()


        

class Bishop(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves():
        if (super().color == "white"):
            #it can only move up that column, or capture in adjacent columns.
            print()
        else:
            #it can only move down
            print()
    
    def __str__(self):
        return self.color + " Bishop @ " + chr(97+self.letter) +","+ self.number.__str__()



        

class Knight(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)
    
    def returnLegalMoves():
        if (super().color == "white"):
            #it can only move up that column, or capture in adjacent columns.
            print()
        else:
            #it can only move down
            print()
    
    def __str__(self):
        return self.color + "Knight @" + chr(97+self.letter) +","+ self.number.__str__()



        

class Rook(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

    def returnLegalMoves():
        if (super().color == "white"):
            #it can only move up that column, or capture in adjacent columns.
            print()
        else:
            #it can only move down
            print()
    
    def __str__(self):
        return self.color + "Rook @" + chr(97+self.letter) +","+ self.number.__str__()


