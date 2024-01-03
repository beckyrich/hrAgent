from nest.core import Controller, Get, Post, Depends

from src.jobs.jobs_service import JobsService
from src.jobs.jobs_model import Jobs


@Controller("jobs")
class JobsController:

    service: JobsService = Depends(JobsService)
    
    @Get("/get_jobs")
    def get_jobs(self):
        return self.service.get_jobs()
                
    @Post("/add_jobs")
    def add_jobs(self, jobs: Jobs):
        return self.service.add_jobs(jobs)
 