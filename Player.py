from Company import Company


class Player:

    player_profit: int = 0
    player_resources: int = 0
    position_on_the_board: int = 0

    def __init__(self):
        self.player_name = input("Your name: ")
        self.owned_company_name = input("Your company name: ")
        self.owned_company = Company()

    def update_resources(self, resources: int):
        self.player_resources += resources

    def initial_resources_allocation(self):
        marketing = 0
        efficiency = 0
        innovation = 0
        marketing = self._check_consistency("marketing", marketing, efficiency, innovation)
        efficiency = self._check_consistency("efficiency", marketing, efficiency, innovation)
        innovation = self._check_consistency("innovation", marketing, efficiency, innovation)
        self.owned_company.update_intrinsics(marketing, efficiency, innovation)

    def update_profit(self, profit: int):
        self.player_resources += profit

    def _check_consistency(self,intrinsic:str, marketing, efficiency, innovation) -> int:

        class FinishedResourcesError(Exception):
            def __init__(self):
                print("Not enough resources. ")

        while True:
            try:
                resource_input = int(input(f"How many to {intrinsic}: "))
                if resource_input + marketing + efficiency + innovation > self.player_resources:
                    raise FinishedResourcesError
            except ValueError:
                print("You have to input a number.")
                continue
            except FinishedResourcesError:
                continue
            else:
                return resource_input
