import Const as C


class Company:

    def __init__(self):
        self.number_of_clients: int = C.NUMBER_OF_CLIENTS
        self.selling_price: int = C.SELLING_PRICE

        self.profit_and_losses = {
            "revenue": C.REVENUE,
            "costs": C.COSTS,
            "profit": C.PROFIT
        }
        self.intrinsics = {
            "marketing": C.MARKETING,
            "efficiency": C.EFFICIENCY,
            "innovation": C.INNOVATION
        }

    def update_number_of_clients(self, player_to_compare):
        if self.intrinsics["marketing"] <= player_to_compare.owned_company.intrinsics["marketing"]:
            return None
        else:
            delta = self.intrinsics["marketing"] - player_to_compare.owned_company.intrinsics["marketing"]
            self.number_of_clients += delta
            if delta > player_to_compare.owned_company.number_of_clients:
                player_to_compare.owned_company.number_of_clients = 0
            else:
                player_to_compare.owned_company.number_of_clients -= delta

    def update_price(self):
        print(f"price before {self.selling_price}")
        self.selling_price += self.intrinsics["innovation"]
        print(f"price after {self.selling_price}")

    def update_profit_and_losses(self):
        self.profit_and_losses["revenue"] = self.number_of_clients * self.selling_price
        self.profit_and_losses["costs"] = self.number_of_clients - self.intrinsics["efficiency"]
        self.profit_and_losses["profit"] = self.profit_and_losses["revenue"] - self.profit_and_losses["costs"]

    def update_intrinsics(self, marketing: int = 0, efficiency: int = 0, innovation: int = 0):
        self.intrinsics["marketing"] += marketing
        self.intrinsics["efficiency"] += efficiency
        self.intrinsics["innovation"] += innovation
