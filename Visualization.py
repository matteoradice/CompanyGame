import Player
from prettytable import PrettyTable


visualizer = PrettyTable()

def visualize(player:Player):
    print("********************************************")
    print(player.player_name)
    print(player.owned_company_name)
    print("********************************************")
    visualizer.field_names = ["Items", "Company Data", "P&L", "Other"]
    visualizer.add_rows(
        [
            ["Number of clients", str(player.owned_company.number_of_clients), " - ", " - "],
            ["Total profit", str(player.player_profit), " - ", " - "],
            ["Remaining resources", str(player.player_resources), " - ", " - "],
            ["Revenues", " - ", str(player.owned_company.profit_and_losses['revenue']), " - "],
            ["Costs", " - ", str(player.owned_company.profit_and_losses['costs']), " - "],
            ["Turn profit", " - ", str(player.owned_company.profit_and_losses['profit']), " - "],
            ["Marketing points", " - ", " - ", str(player.owned_company.intrinsics['marketing'])],
            ["Innovation points", " - ", " - ", str(player.owned_company.intrinsics['innovation'])],
            ["Efficiency points", " - ", " - ", str(player.owned_company.intrinsics['efficiency'])],
        ]
    )
    print(visualizer)
    print("\n")
