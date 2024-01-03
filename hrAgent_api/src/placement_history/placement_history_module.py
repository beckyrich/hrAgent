from src.placement_history.placement_history_service import PlacementHistoryService
from src.placement_history.placement_history_controller import PlacementHistoryController


class PlacementHistoryModule:

    def __init__(self):
        self.providers = [PlacementHistoryService]
        self.controllers = [PlacementHistoryController]



