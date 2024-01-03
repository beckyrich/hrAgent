from nest.core import Controller, Get, Post, Depends

from src.candidate.candidate_service import CandidateService
from src.candidate.candidate_model import Candidate


@Controller("candidate")
class CandidateController:

    service: CandidateService = Depends(CandidateService)
    
    @Get("/get_candidate")
    def get_candidate(self):
        return self.service.get_candidate()
                
    @Post("/add_candidate")
    def add_candidate(self, candidate: Candidate):
        return self.service.add_candidate(candidate)
 