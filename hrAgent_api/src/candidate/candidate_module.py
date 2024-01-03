from src.candidate.candidate_service import CandidateService
from src.candidate.candidate_controller import CandidateController


class CandidateModule:

    def __init__(self):
        self.providers = [CandidateService]
        self.controllers = [CandidateController]



