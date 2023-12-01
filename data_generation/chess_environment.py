
import chess
from trait_mapping import TraitMapping
from chess_transformer import ChessTransformer, TraitEncoder, ExplainableChessTransformer

class ChessGame:
    def __init__(self, player1_trait, player2_trait):
        self.board = chess.Board()
        self.trait_encoder = TraitEncoder()
        self.chess_transformer = ChessTransformer(self.trait_encoder)
        self.explainable_transformer = ExplainableChessTransformer(self.chess_transformer)
        self.player1_trait = player1_trait
        self.player2_trait = player2_trait

    def make_move(self, move):
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

    def get_best_move(self, trait):
        # Here, we use the transformer model to decide the best move
        board_fen = self.board.fen()
        move = self.explainable_transformer(board_fen, trait)
        return move

    def simulate_game(self):
        while True:
            if self.board.turn:
                move = self.get_best_move(self.player1_trait)
            else:
                move = self.get_best_move(self.player2_trait)

            if not self.make_move(move):
                return "Invalid move"

            status = self.game_status()
            if status != "Game in progress":
                return status