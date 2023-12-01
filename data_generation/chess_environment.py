
import chess
class ChessGame:
    def __init__(self, trait):
        self.board = chess.Board()
        self.trait = trait

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

    def calculate_best_aggressive_move(self, board):
        # 1. List all legal moves
        # 2. Prioritize moves that:
        #    - Capture opponent's pieces, especially near the opponent's king
        #    - Put the opponent's king in check
        #    - Open lines for attacking the opponent's king
        # 3. Select the move that maximizes positional advantage or material gain
        #    (This may require an evaluation function)        
        legal_moves = list(board.legal_moves)
        best_move = None
        best_score = float('-inf')

        for move in legal_moves:
            # Make a copy of the board to simulate the move
            temp_board = board.copy()
            temp_board.push(move)

            # Evaluate the move based on capturing opponent's pieces, checking the opponent's king, and opening lines for attacking the opponent's king
            score = self.evaluate_move(temp_board, self.trait)

            # Update the best move if the current move has a higher score
            if score > best_score:
                best_move = move
                best_score = score

        return best_move

    def evaluate_move(self, board, trait):
        # Define weights for different traits
        capture_weight, check_weight, open_lines_weight = self.get_trait_weights(trait)

        score = 0

        # Capture opponent's pieces
        captured_piece = board.piece_at(board.peek())
        if captured_piece is not None:
            score += capture_weight * captured_piece.piece_type

        # Check the opponent's king
        if board.is_check():
            score += check_weight

        # Open lines for attacking the opponent's king
        for square in board.attackers(not board.turn, board.king(not board.turn)):
            score += open_lines_weight

        return score
    
    def get_trait_weights(self, trait):
        if trait == "Aggressive":
            return 3, 2, 1  # Prioritize captures and checks
        elif trait == "Skeptical":
            return 1, 1, 1  # Balanced approach
        elif trait == "Cautious":
            return 1, 2, 3  # Prioritize open lines and safety
        elif trait == "Innovative":
            return 2, 3, 1  # Prioritize unusual moves and checks
        else:
            return 1, 1, 1  # Default weights
    
    def calculate_best_skeptical_move(self, board):
        # 1. List all legal moves
        # 2. Prioritize moves that:
        #    - Reinforce your own position (e.g., developing pieces, controlling the center)
        #    - Avoid unnecessary risks (e.g., premature attacks, uncalculated sacrifices)
        #    - Focus on solidifying your position rather than attacking
        #  use evaluate_move(board) to evaluate the move
        legal_moves = list(board.legal_moves)
        best_move = None
        best_score = float('-inf')

        for move in legal_moves:
            # Make a copy of the board to simulate the move
            temp_board = board.copy()
            temp_board.push(move)

            # Evaluate the move based on reinforcing own position, avoiding unnecessary risks, and focusing on solidifying position
            score = self.evaluate_move(temp_board, self.trait)

            # Update the best move if the current move has a higher score
            if score > best_score:
                best_move = move
                best_score = score

        return best_move        

    def calculate_best_cautious_move(self, board):
        legal_moves = list(board.legal_moves)
        best_move = None
        best_score = float('-inf')

        for move in legal_moves:
            # Make a copy of the board to simulate the move
            temp_board = board.copy()
            temp_board.push(move)

            # Evaluate the move based on reinforcing own position, avoiding unnecessary risks, and focusing on solidifying position
            score = self.evaluate_move(temp_board, self.trait)

            # Update the best move if the current move has a higher score
            if score > best_score:
                best_move = move
                best_score = score

        return best_move
        
    def calculate_best_innovative_move(self, board):
        legal_moves = list(board.legal_moves)
        best_move = None
        best_score = float('-inf')

        for move in legal_moves:
            # Make a copy of the board to simulate the move
            temp_board = board.copy()
            temp_board.push(move)

            # Evaluate the move based on potential benefits and risks
            score = self.evaluate_move(temp_board, self.trait)

            # Update the best move if the current move has a higher score
            if score > best_score:
                best_move = move
                best_score = score

        return best_move
        
    def simulate_game(self, player1, player2):
        while True:
            if self.board.turn:
                if self.trait == "Aggressive":
                    move = self.calculate_best_aggressive_move(self.board)
                elif self.trait == "Skeptical":
                    move = self.calculate_best_skeptical_move(self.board)
                elif self.trait == "Cautious":
                    move = self.calculate_best_cautious_move(self.board)
                elif self.trait == "Innovative":
                    move = self.calculate_best_innovative_move(self.board)
                else:
                    move = player1.get_move(self.board)
            else:
                move = player2.get_move(self.board)

            if not self.make_move(move):
                return "Invalid move"
            
            status = self.game_status()
            if status != "Game in progress":
                return status
