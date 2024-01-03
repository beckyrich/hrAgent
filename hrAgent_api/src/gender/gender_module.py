from src.gender.gender_service import GenderService
from src.gender.gender_controller import GenderController


class GenderModule:

    def __init__(self):
        self.providers = [GenderService]
        self.controllers = [GenderController]



