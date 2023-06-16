import random
from Player import Player
from BoardSquares import board_squares


class GameBox:
    turn: int = 0
    clients_remaining = 100
    resources_remaining = 20
    number_of_players = 2
    dice_score = 0

    chances_cards = [{
        "text": "best marketing ever",
        "marketing": 2
    }]
    market_events_cards = [{
        "text": "best marketing ever",
        "marketing": 2
    }]

    def __init__(self):
        self.squares = self.create_board()

    def create_board(self, number_of_squares: int = 39) -> []:
        board = []
        for i in range(0, number_of_squares):
            board.append(random.choice(board_squares))
        return board

    def roll_dices(self):
        self.dice_score = random.randint(1, 6)

    def initial_set_up(self, player: Player):
        clients_to_distribute = self.clients_remaining / self.number_of_players
        player.owned_company.number_of_clients = clients_to_distribute
        resources_to_distribute = self.resources_remaining / self.number_of_players
        player.player_resources = resources_to_distribute

    def manage_turn(self, player: Player):
        # Initialize function attributes
        dices_score = 0

        # Roll the dices
        self.roll_dices()
        print(f"Dice roll: {self.dice_score}")
        dices_score += self.dice_score
        self.roll_dices()
        dices_score += self.dice_score
        print(f"Dice roll: {self.dice_score}")
        print(f"Total dice score: {dices_score}")

        # Move to a square
        active_square = self.squares[dices_score - 1]
        print(f"You ended up on:")
        print(active_square)

        # Apply square effects on player
        for i in active_square:
            for x in player.owned_company.intrinsics:
                if i == x:
                    player.owned_company.intrinsics[i] += active_square[i]

        # Update turn
        self.turn += 1
