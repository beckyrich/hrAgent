from nest.core import Controller, Get, Post, Depends

from src.states.states_service import StatesService
from src.states.states_model import States


@Controller("states")
class StatesController:

    service: StatesService = Depends(StatesService)
        
    @Get("/")
    def get_state_by_abbv(self, abbv: str = None):
        if abbv:
            print("Abbreviation Found:", abbv)
            return self.service.get_one_state(abbv)
        return self.service.get_states()
                
    @Post("/add")
    def add_states(self, states: States):
        return self.service.add_states(states)
 