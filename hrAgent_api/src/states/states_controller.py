from nest.core import Controller, Get, Post, Depends

from src.states.states_service import StatesService
from src.states.states_model import States


@Controller("states")
class StatesController:

    service: StatesService = Depends(StatesService)
    
    @Get("/get_states")
    def get_states(self):
        return self.service.get_states()
                
    @Post("/add_states")
    def add_states(self, states: States):
        return self.service.add_states(states)
 