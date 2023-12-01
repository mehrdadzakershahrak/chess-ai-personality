# Pseudocode for generating self-play data
class SelfPlayGenerator:
    def generate_games(self, number_of_games):
        games_data = []
        for _ in range(number_of_games):
            # Initialize players with traits
            player1_trait, player2_trait = self.randomly_select_traits()
            game_result = self.play_game(player1_trait, player2_trait)
            games_data.append((game_result, player1_trait, player2_trait))
        return games_data

    # Function to simulate a game between two players with given traits
    def play_game(self, player1_trait, player2_trait):
        # Play a game and return the result with tagged traits
        pass