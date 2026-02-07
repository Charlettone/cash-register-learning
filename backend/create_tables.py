from app.database import engine
from app.models.user import User
from app.database import Base

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
