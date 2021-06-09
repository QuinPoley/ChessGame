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
        return self.color + "pawn @" + self.letter.__str__() +","+ self.number.__str__()

        

class King(Piece):
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

        

class Queen:
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

        

class Bishop:
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

        

class Knight:
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

        

class Rook:
    def __init__(self, color, letter, number):
        super().__init__(color, letter, number)

