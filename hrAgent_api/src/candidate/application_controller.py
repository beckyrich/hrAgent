from nest.core import Controller, Get, Post, Depends

from src.candidate.application_service import ApplicationService
from src.candidate.candidate_model import Application, ApplicationUpdate


@Controller("application")
class ApplicationController:
    service: ApplicationService = Depends(ApplicationService)

    @Get("/all")
    def get_all_applications(self):
        return self.service.get_all_applications()

    @Post("/create")
    def create_an_app(self, app_form: Application):
        return self.service.create_an_app(app_form)
