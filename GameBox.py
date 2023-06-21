import random

import Const as C
import Dice
from Player import Player
from BoardSquares import board_squares


class GameBox:
    turn: int = C.TURN
    clients_remaining = C.TOTAL_CLIENTS
    resources_remaining = C.TOTAL_RESOURCES
    number_of_players = C.NUMBER_OF_PLAYERS
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

    def create_board(self, number_of_squares: int = C.NUMBER_OF_SQUARES) -> []:
        board = []
        for i in range(0, number_of_squares):
            board.append(random.choice(board_squares))
        return board

    def roll_dices(self):
        self.dice_score = random.randint(1, 6)
        visual_dice = Dice.dice[self.dice_score]
        print(f"Dice roll: {visual_dice}")

    def initial_set_up(self, player: Player):
        clients_to_distribute = self.clients_remaining / self.number_of_players
        player.owned_company.number_of_clients = clients_to_distribute
        resources_to_distribute = self.resources_remaining / self.number_of_players
        player.player_resources = resources_to_distribute

    def manage_turn(self, player: Player):
        # Initialize function attributes
        dices_score = 0

        # Roll the dices
        for i in range(0,1):
            self.roll_dices()
            dices_score += self.dice_score
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
