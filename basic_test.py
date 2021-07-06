# Basic Tests for the application
from game import GameOfChess
import LegalMove
import pieces

# Assert that the game starts okay
def test_gameInitializeOk():
    game = GameOfChess()
    assert type(game.Black) == list
    assert type(game.White) == list
    assert len(game.Black) == 16
    assert len(game.White) == 16

# Assert we can select pieces
def test_selectPieceOk():
    game = GameOfChess()
    wKing = LegalMove.getPosKing(game.White)
    game.CurrentlySelected = wKing
    assert type(wKing) == pieces.King
    assert wKing.letter == 5
    assert wKing.number == 1
    assert game.CurrentlySelected == wKing

# Assert that we can move pieces
def test_movePieceOk():
    game = GameOfChess()
    wKingPawn = LegalMove.getPieceAtSquare(5, 2, game.White)
    assert wKingPawn.hasMoved == False
    game.CurrentlySelected = wKingPawn
    game.MovePiece((5, 4), True)
    assert wKingPawn.number == 4
