from orm_config import config
from nest.core.app import App
from fastapi.responses import RedirectResponse
from src.examples.examples_module import ExamplesModule
from src.company.company_module import CompanyModule
from src.candidate.candidate_module import CandidateModule
from src.placement_history.placement_history_module import PlacementHistoryModule
from src.jobs.jobs_module import JobsModule
from src.gender.gender_module import GenderModule
from src.master_company.master_company_module import MasterCompanyModule
from src.states.states_module import StatesModule

# FastAPI docs says to put below in main.py but decided to put it here (Security- First Steps)
from typing import Annotated
from nest.core import Depends
from src.auth.auth import oauth2_scheme
from src.auth.auth import app as authRouter


app = App(
    description="PyNest service",
    title="Our HR Agent",
    modules=[
        ExamplesModule,
        CompanyModule,
        CandidateModule,
        PlacementHistoryModule,
        JobsModule,
        GenderModule,
        MasterCompanyModule,
        StatesModule,
    ],
)

app.include_router(authRouter)

@app.on_event("startup")
async def startup():
    config.create_all()


@app.get("/")
async def index():
    return RedirectResponse(url=app.docs_url)
