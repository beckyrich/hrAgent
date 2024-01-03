from nest.core import Controller, Get, Post, Depends

from src.gender.gender_service import GenderService
from src.gender.gender_model import Gender


@Controller("gender")
class GenderController:

    service: GenderService = Depends(GenderService)
    
    @Get("/get_gender")
    def get_gender(self):
        return self.service.get_gender()
                
    @Post("/add_gender")
    def add_gender(self, gender: Gender):
        return self.service.add_gender(gender)
 