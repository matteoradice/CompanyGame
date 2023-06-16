from GameBox import GameBox
from Player import Player
import Visualization as v


gameBox = GameBox()
player_one = Player()
gameBox.initial_set_up(player_one)
player_one.initial_resources_allocation()

player_two = Player()
gameBox.initial_set_up(player_two)
player_two.initial_resources_allocation()

v.visualize(player_one)
v.visualize(player_two)

player_one.owned_company.update_intrinsics()
print(player_one.owned_company.intrinsics)
player_one.owned_company.update_number_of_clients(player_two)
player_one.owned_company.update_price()
print(player_one.owned_company.selling_price)
player_one.owned_company.update_profit_and_losses()

v.visualize(player_one)
v.visualize(player_two)

gameBox.manage_turn(player_one)
v.visualize(player_one)