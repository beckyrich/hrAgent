from nest.core.database.orm_provider import OrmProvider
import os
from dotenv import load_dotenv

load_dotenv()

config = OrmProvider(
    db_type="postgresql",
    config_params=dict(
        db_name="hragent",
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5433"),
    ),
)
