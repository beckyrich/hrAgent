from orm_config import config
from nest.core.app import App
from fastapi.responses import RedirectResponse
from src.examples.examples_module import ExamplesModule
from src.company.company_module import CompanyModule
from src.candidate.candidate_module import CandidateModule

app = App(
    description="PyNest service",
    title="Our HR Agent",
    modules=[
        ExamplesModule,
        CompanyModule,
        CandidateModule,
    ]
)


@app.on_event("startup")
async def startup():
    config.create_all() 


@app.get("/")
async def index():
    return RedirectResponse(url=app.docs_url)
