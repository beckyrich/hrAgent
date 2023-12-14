from nest.core import Controller, Get, Post, Depends

from src.examples.examples_service import ExamplesService
from src.examples.examples_model import Examples


@Controller("examples")
class ExamplesController:

    service: ExamplesService = Depends(ExamplesService)
    
    @Get("/get_examples")
    def get_examples(self):
        return self.service.get_examples()
                
    @Post("/add_examples")
    def add_examples(self, examples: Examples):
        return self.service.add_examples(examples)
 