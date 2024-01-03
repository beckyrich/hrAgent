from src.states.states_service import StatesService
from src.states.states_controller import StatesController


class StatesModule:

    def __init__(self):
        self.providers = [StatesService]
        self.controllers = [StatesController]



