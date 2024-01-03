from nest.core import Controller, Get, Post, Depends

from src.placement_history.placement_history_service import PlacementHistoryService
from src.placement_history.placement_history_model import PlacementHistory


@Controller("placement_history")
class PlacementHistoryController:

    service: PlacementHistoryService = Depends(PlacementHistoryService)
    
    @Get("/get_placement_history")
    def get_placement_history(self):
        return self.service.get_placement_history()
                
    @Post("/add_placement_history")
    def add_placement_history(self, placement_history: PlacementHistory):
        return self.service.add_placement_history(placement_history)
 