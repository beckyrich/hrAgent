from nest.core.database.base_orm import OrmService
import os
from dotenv import load_dotenv

load_dotenv()
    
config = OrmService(
    db_type="sqlite",
    config_params=dict(
        db_name=os.getenv("SQLITE_DB_NAME", "default_nest_db"),
    )
)
        