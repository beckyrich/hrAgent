from src.candidate.candidate_service import CandidateService
from src.candidate.candidate_controller import CandidateController
from src.candidate.application_controller import ApplicationController
from src.candidate.application_service import ApplicationService


class CandidateModule:
    def __init__(self):
        self.providers = [CandidateService, ApplicationService]
        self.controllers = [CandidateController, ApplicationController]
