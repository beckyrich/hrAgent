from nest.core import Controller, Get, Post, Depends

from src.candidate.application_service import ApplicationService
from src.candidate.candidate_model import Application, ApplicationUpdate

def user_auth_sample(api_key: str):
    return True


@Controller("application")
class ApplicationController:
    service: ApplicationService = Depends(ApplicationService)

    @Get("/all")
    def get_all_applications(self, api_key: str = Depends(user_auth_sample)):
        return self.service.get_all_applications()

    @Post("/create")
    def create_an_app(self, app_form: Application):
        return self.service.create_an_app(app_form)
