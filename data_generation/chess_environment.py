
import chess

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def make_move(self, move):
        # Ensure the move is legal
        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        return False

    def game_status(self):
        if self.board.is_checkmate():
            return "Checkmate"
        elif self.board.is_stalemate():
            return "Stalemate"
        elif self.board.is_insufficient_material():
            return "Insufficient material"
        elif self.board.is_seventyfive_moves():
            return "Draw due to 75 moves rule"
        elif self.board.is_fivefold_repetition():
            return "Draw due to fivefold repetition"
        elif self.board.is_variant_draw():
            return "Draw due to variant-specific rules"
        else:
            return "Game in progress"

    def simulate_game(self, player1, player2):
        while True:
            if self.board.turn:
                move = player1.get_move(self.board)
            else:
                move = player2.get_move(self.board)

            if not self.make_move(move):
                return "Invalid move"
            
            status = self.game_status()
            if status != "Game in progress":
                return status
