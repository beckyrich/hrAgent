from src.jobs.jobs_service import JobsService
from src.jobs.jobs_controller import JobsController


class JobsModule:

    def __init__(self):
        self.providers = [JobsService]
        self.controllers = [JobsController]



