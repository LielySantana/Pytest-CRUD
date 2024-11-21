from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///.test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def init_db():
    import app.models as models
    models.Base.metadata.create_all(bind=engine)